# Experiment 1: Install Apache Kafka on a single node

Since you have already installed Apache Kafka using Docker on Windows, this experiment is largely complete! 

## Prerequisites
- Docker Desktop running on Windows.
- `docker-compose.yml` file configured with Zookeeper and Kafka services.

## Steps to Verify Installation
1. Open a terminal (PowerShell or Command Prompt) in the directory containing your `docker-compose.yml`.
2. Start the Kafka cluster:
   ```bash
   docker-compose up -d
   ```
3. Check if the containers are running:
   ```bash
   docker ps
   ```
   You should see both Zookeeper and Kafka containers up and running.
4. To stop the cluster later, you can run:
   ```bash
   docker-compose down
   ```
