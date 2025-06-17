# EmoStream: Real-time Emoji Processing System

A high-performance, event-driven system for concurrent emoji broadcasting and processing using Kafka and Flask.

## Overview

EmoStream is a distributed system that enables real-time emoji broadcasting and processing. It uses an event-driven architecture with Kafka as the message broker to handle concurrent emoji submissions and broadcasting to multiple subscribers.

## Architecture

The system consists of the following components:

1. **API Server (Flask)**
   - Handles client registration and emoji submissions
   - Publishes emoji events to Kafka
   - RESTful endpoints for client management

2. **Kafka Message Broker**
   - Handles message queuing and distribution
   - Ensures reliable message delivery
   - Supports concurrent message processing

3. **Subscribers**
   - Multiple subscriber instances for load distribution
   - Process emoji events in real-time
   - Maintain individual client connections

## Features

- Real-time emoji broadcasting
- Concurrent client support
- Event-driven architecture
- Scalable subscriber system
- RESTful API for client management
- Health monitoring and logging
- Docker containerization

## Prerequisites

- Docker
- Docker Compose
- Python 3.9+
- Kafka (provided via Docker)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/EmoStream.git
cd EmoStream
```

2. Build and start the containers:
```bash
docker-compose up --build
```

## API Endpoints

- `POST /register` - Register a new client
- `POST /emoji` - Send an emoji
- `DELETE /deregister` - Deregister a client
- `GET /clients` - List all registered clients

## Testing

The project includes comprehensive test suites:

1. **API Tests** (`test/test_api.py`)
   - Tests client registration
   - Tests emoji submission
   - Tests client deregistration

2. **Streaming Tests** (`test/test_streaming.py`)
   - Simulates concurrent client behavior
   - Tests message delivery
   - Tests system performance

Run tests using:
```bash
docker-compose up test
```

## Configuration

The system can be configured through environment variables:

- `KAFKA_BROKER`: Kafka broker address (default: localhost:9092)
- `FLASK_APP`: Flask application entry point
- `FLASK_ENV`: Environment (development/production)

## Monitoring

- Container health checks
- Logging to `/app/logs`
- Kafka topic monitoring
- Client connection tracking

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Kafka for message queuing
- Flask for the web framework
- Docker for containerization
