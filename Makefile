.PHONY: build up down test logs clean

# Build and start all services
up:
	docker-compose up --build -d

# Start services in foreground
up-fg:
	docker-compose up --build

# Stop all services
down:
	docker-compose down

# Run tests
test:
	docker-compose up test

# View logs
logs:
	docker-compose logs -f

# View logs for specific service
logs-app:
	docker-compose logs -f app

logs-kafka:
	docker-compose logs -f kafka

logs-subscriber:
	docker-compose logs -f subscriber

# Clean up containers and volumes
clean:
	docker-compose down -v --remove-orphans
	docker system prune -f

# Build only
build:
	docker-compose build

# Restart services
restart:
	docker-compose restart

# Status
status:
	docker-compose ps
