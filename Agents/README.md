Docker Compose File README
This Docker Compose file sets up three services: cadvisor, node-exporter, and promtail, all of which are part of a network named web_net.

Services
1. cadvisor
The cadvisor service uses the gcr.io/cadvisor/cadvisor image and is configured to restart always. It has several volumes mounted for monitoring purposes and is labeled for use with Traefik as a reverse proxy. The labels include configuration for both HTTP and HTTPS entrypoints, redirection from HTTP to HTTPS, and the use of a middleware named web-auth. The service is also part of the web_net network.

2. node-exporter
The node-exporter service uses the prom/node-exporter:v1.3.1 image and is also configured to restart always. It has several volumes mounted for monitoring purposes and is labeled for use with Traefik as a reverse proxy, similar to the cadvisor service. The service is also part of the web_net network.

3. promtail
The promtail service uses the grafana/promtail:k116-a1dce32 image and is configured to restart always. It has a volume mounted for log files and another for its configuration file. The service is also part of the web_net network.

Networks
The web_net network is defined as external and must be created before running docker-compose up.

Usage
To use this Docker Compose file, you need to replace the placeholders (e.g., ${HOSTNAME}, ${CSUB}, ${NSUB}, {{inventory_hostname}}, ${domain}) with your actual values. Then, you can run the services using the command docker-compose up.

Please note that you need to have Docker and Docker Compose installed on your machine to use this file. Also, ensure that the web_net network is created before running the services. You can create the network using the command docker network create web_net.

Important
This Docker Compose file is configured to use Traefik as a reverse proxy. Make sure you have Traefik set up correctly and the necessary middlewares (e.g., web-auth, https-redirect) are defined in your Traefik configuration. Also, ensure that you have a certificate resolver named mycert configured in Traefik for HTTPS support.

This is a basic overview of the Docker Compose file. For more detailed information, please refer to the documentation of each individual service and Docker Compose.
