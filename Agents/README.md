# Docker Compose Configuration for Monitoring Stack

This Docker Compose configuration sets up a monitoring stack using cAdvisor, Node Exporter, and Promtail. Traefik is used as a reverse proxy for secure access to the services.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Configuration](#configuration)
  - [Running the Services](#running-the-services)
- [Services](#services)
  - [cAdvisor](#cadvisor)
  - [Node Exporter](#node-exporter)
  - [Promtail](#promtail)
- [Traefik Configuration](#traefik-configuration)
- [Networks](#networks)
- [Volumes](#volumes)
- [Additional Notes](#additional-notes)
- [License](#license)

## Prerequisites

Ensure you have Docker and Docker Compose installed on your system.

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Getting Started
Configuration
Before running the services, modify the .env file with your specific configurations, including ${HOSTNAME}, ${CSUB}, ${NSUB}, and ${domain}.

Running the Services
Run the monitoring stack using the following command:

```bash
Copy code
docker-compose up -d
This will start cAdvisor, Node Exporter, and Promtail.
```
Services
cAdvisor
cAdvisor provides container usage information.

Access cAdvisor at http://your_domain_or_ip.

Node Exporter
Node Exporter exports system metrics from the host machine.

Access Node Exporter at http://your_domain_or_ip:9100.

Promtail
Promtail is used for log collection.

Traefik Configuration
Traefik is configured to handle routing and SSL termination. Update Traefik labels in the docker-compose.yml file as needed.

Networks
The services are connected to the web_net Docker network.

Volumes
Volumes are mounted for data persistence and configuration files.

Additional Notes
Ensure the necessary ports are open in your firewall.
Customize Traefik labels for your specific domain.
Adjust security measures as needed for your environment.

