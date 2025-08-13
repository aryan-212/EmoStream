from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import threading
import time
import random  # Missing import

app = Flask(__name__)

@app.route('/') 
def health_check():
    """Health check endpoint for Docker."""
    return jsonify({"status": "healthy", "service": "EmoStream API"}), 200

import os

# Initialize the Kafka producer with retry logic
kafka_broker = os.getenv('KAFKA_BROKER', 'localhost:9092')

def create_kafka_producer():
    """Create Kafka producer with retry logic."""
    max_retries = 30
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            print(f"Attempting to connect to Kafka at {kafka_broker} (attempt {attempt + 1}/{max_retries})")
            producer = KafkaProducer(
                bootstrap_servers=[kafka_broker],
                value_serializer=lambda x: json.dumps(x).encode('utf-8')
            )
            print("Successfully connected to Kafka!")
            return producer
        except Exception as e:
            print(f"Failed to connect to Kafka (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Exiting.")
                raise

producer = create_kafka_producer()

# A flag to manage the flushing thread
flushing = True
flush_lock = threading.Lock()  # Lock for thread-safe access to the flushing flag

# Store subscriber information
subscribers = [
    {"cluster_id": 0, "subscriber_id": 0, "port": 6000},
    {"cluster_id": 0, "subscriber_id": 1, "port": 6001},
    {"cluster_id": 0, "subscriber_id": 2, "port": 6002},
    {"cluster_id": 1, "subscriber_id": 0, "port": 6003},
    {"cluster_id": 1, "subscriber_id": 1, "port": 6004},
    {"cluster_id": 1, "subscriber_id": 2, "port": 6005},
    {"cluster_id": 2, "subscriber_id": 0, "port": 6006},
    {"cluster_id": 2, "subscriber_id": 1, "port": 6007},
    {"cluster_id": 2, "subscriber_id": 2, "port": 6008},
]
client_assignments = {}

@app.route('/register_client', methods=['POST'])
def register_client():
    client_data = request.get_json()
    client_id = client_data.get("client_id")

    if not client_id:
        return jsonify({"error": "client_id is required"}), 400

    # Check if the client is already assigned
    if client_id in client_assignments:
        assigned_subscriber = client_assignments[client_id]
        return jsonify({
            "message": f"Client {client_id} is already registered.",
            "assigned_subscriber": assigned_subscriber
        }), 200

    # Assign a random subscriber
    assigned_subscriber = random.choice(subscribers)
    client_assignments[client_id] = assigned_subscriber

    return jsonify({
        "message": f"Client {client_id} successfully registered.",
        "assigned_subscriber": assigned_subscriber
    }), 200

def flush_kafka_producer(interval=0.5):
    """Flush Kafka producer at regular intervals."""
    global flushing
    while flushing:
        time.sleep(interval)
        with flush_lock:
            if flushing:
                producer.flush()

# Start a thread to periodically flush the Kafka producer
flush_thread = threading.Thread(target=flush_kafka_producer, args=(0.5,), daemon=True)
flush_thread.start()

@app.route('/emoji', methods=['POST'])
def send_emoji():
    try:
        # Get emoji data from the request body
        data = request.get_json()
        print(data)
        emoji = data.get("emoji_type", "")
        
        if not emoji:
            return jsonify({"error": "No emoji provided"}), 400

        # Publish emoji to the 'emoji_stream' Kafka topic
        producer.send('emoji_stream', value={
            "timestamp": data.get("timestamp", ""),
            "emoji_type": emoji
        })
        
        return jsonify({"message": "Emoji sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/deregister_client', methods=['POST'])
def deregister_client():
    client_data = request.get_json()
    client_id = client_data.get("client_id")

    if not client_id:
        return jsonify({"error": "client_id is required"}), 400

    # Check if the client is registered
    if client_id not in client_assignments:
        return jsonify({"error": "Client not found"}), 404

    # Remove the client from the assignments
    del client_assignments[client_id]
    return jsonify({"message": f"Client {client_id} deregistered successfully"}), 200
@app.route('/list_clients', methods=['GET'])
def list_clients():
    """Endpoint to list all registered clients and their assignments."""
    return jsonify(client_assignments), 200

@app.route('/shutdown', methods=['POST'])
def shutdown():
    """Endpoint to safely shut down the app."""
    global flushing
    with flush_lock:
        flushing = False
    flush_thread.join()  # Ensure the flush thread has completed before shutting down
    producer.close()
    return jsonify({"message": "Producer and app shut down successfully"}), 200

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        # Gracefully handle shutdown on interrupt
        with flush_lock:
            flushing = False
        flush_thread.join()
        producer.close()
