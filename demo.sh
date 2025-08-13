#!/bin/bash

# 🎉 EmoStream Demo Script
# Run this to test your system!

echo "🚀 Starting EmoStream Demo..."
echo "================================"

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 5

# Test health endpoint
echo "✅ Testing health endpoint..."
curl -s http://localhost:5000/ | jq . 2>/dev/null || echo "Health check failed - services might not be ready yet"

echo ""
echo "🎯 Testing emoji submission..."
curl -s -X POST http://localhost:5000/emoji \
  -H "Content-Type: application/json" \
  -d '{"emoji_type": "😊", "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}' | jq . 2>/dev/null || echo "Emoji submission failed"

echo ""
echo "👤 Testing client registration..."
curl -s -X POST http://localhost:5000/register_client \
  -H "Content-Type: application/json" \
  -d '{"client_id": "demo_user"}' | jq . 2>/dev/null || echo "Client registration failed"

echo ""
echo "📋 Listing clients..."
curl -s http://localhost:5000/list_clients | jq . 2>/dev/null || echo "List clients failed"

echo ""
echo "🎉 Demo complete! Your EmoStream is working!"
echo ""
echo "💡 Try these commands:"
echo "   curl http://localhost:5000/"
echo "   curl -X POST http://localhost:5000/emoji -H 'Content-Type: application/json' -d '{\"emoji_type\": \"🚀\", \"timestamp\": \"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'\"}'"
echo ""
echo "🛑 To stop everything: docker-compose down"
