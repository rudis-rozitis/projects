# CV Website Project

A comprehensive CV website project for a Junior Infrastructure Engineer with Docker-inspired styling, complete with monitoring and reverse proxy setup.

## Project Overview

This project combines a static CV website with a full monitoring stack, demonstrating infrastructure engineering skills through:
- **CV Website**: A responsive, professionally designed CV with Docker-inspired styling
- **Traefik Reverse Proxy**: Load balancing and routing for all services
- **Prometheus Monitoring**: Metrics collection and monitoring
- **Grafana Dashboards**: Data visualization and monitoring dashboards

## Project Structure

```
cv_project/
├── docker-compose.yml     # Main orchestration file
├── README.md             # This documentation
├── webapp/               # CV Website
│   ├── Dockerfile        # Nginx container configuration
│   ├── index.html        # Main CV page
│   ├── css/
│   │   └── style.css     # Docker-inspired styling
│   ├── js/               # JavaScript files
│   └── images/           # Image assets
├── prometheus/           # Monitoring configuration
│   └── prometheus.yml    # Prometheus scrape configs
└── grafana/              # Dashboard configuration
    └── datasource.yml    # Grafana datasource setup
```

## Prerequisites

- Docker and Docker Compose installed on your system
- Ports 90, 3001, 8080, 9090, and 9100 available

## Quick Start

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd cv_project
```

### 2. Start All Services
```bash
docker-compose up -d
```

### 3. Verify Services
```bash
docker-compose ps
```

## Accessing the Application

### Main CV Website
- **URL**: http://cv.localhost:90
- **Description**: The main CV website with professional layout and Docker-inspired design

### Monitoring Stack

#### Traefik Dashboard
- **URL**: http://localhost:8080
- **Description**: Traefik reverse proxy dashboard showing routing rules and service health

#### Prometheus
- **URL**: http://prometheus.localhost:90 or http://localhost:9090
- **Description**: Prometheus metrics collection interface
- **Features**: 
  - Query metrics using PromQL
  - View targets and configuration
  - Monitor scrape health

#### Grafana
- **URL**: http://grafana.localhost:90 or http://localhost:3001
- **Credentials**: 
  - Username: `admin`
  - Password: `grafana`
- **Description**: Data visualization and monitoring dashboards
- **Pre-configured**: Prometheus datasource automatically configured

## Service Management

### Starting Services
```bash
# Start all services in detached mode
docker-compose up -d

# Start specific service
docker-compose up -d webapp

# View logs for all services
docker-compose logs -f

# View logs for specific service
docker-compose logs -f grafana
```

### Stopping Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clears Prometheus data)
docker-compose down -v

# Stop specific service
docker-compose stop webapp
```

### Rebuilding Services
```bash
# Rebuild and restart all services
docker-compose up -d --build

# Rebuild specific service
docker-compose up -d --build webapp
```

## Monitoring Setup

### Prometheus Configuration
- **Scrape Interval**: 5 seconds
- **Targets**: 
  - Prometheus itself (port 9090)
  - Traefik metrics (port 9100)
- **Configuration**: `prometheus/prometheus.yml`

### Grafana Setup
- **Auto-provisioned datasource**: Prometheus at `http://prometheus:9090`
- **Admin credentials**: admin/grafana
- **Custom dashboards**: Can be added through the UI or by mounting dashboard files

### Traefik Configuration
- **API**: Enabled on port 8080
- **Entrypoints**: 
  - Web traffic: port 90
  - Metrics: port 9100
- **Routing Rules**:
  - `cv.localhost` → CV Website
  - `prometheus.localhost` → Prometheus
  - `grafana.localhost` → Grafana

## Development

### Local Development
For local development without Docker:
```bash
cd webapp
python -m http.server 8000
# Access at http://localhost:8000
```

### Modifying the CV
1. Edit `webapp/index.html` for content changes
2. Edit `webapp/css/style.css` for styling changes
3. Rebuild the webapp service:
   ```bash
   docker-compose up -d --build webapp
   ```

## Troubleshooting

### Common Issues

#### Services not accessible
1. Check if all containers are running:
   ```bash
   docker-compose ps
   ```

2. Check container logs:
   ```bash
   docker-compose logs [service-name]
   ```

#### Port conflicts
If ports are already in use, modify the port mappings in `docker-compose.yml`:
```yaml
ports:
  - "8090:90"  # Change external port from 90 to 8090
```

#### DNS resolution for .localhost domains
If `.localhost` domains don't work, access services directly via localhost:
- CV: http://localhost:90
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3001
- Traefik: http://localhost:8080

### Health Checks
```bash
# Check if all services respond
curl -f http://localhost:90 && echo "CV Website: OK"
curl -f http://localhost:8080 && echo "Traefik: OK"
curl -f http://localhost:9090 && echo "Prometheus: OK"
curl -f http://localhost:3001 && echo "Grafana: OK"
```

### Infrastructure Stack
- **Containerized Deployment** - All services run in Docker containers
- **Reverse Proxy** - Traefik handles routing and load balancing
- **Monitoring** - Prometheus collects metrics from all services
- **Visualization** - Grafana provides dashboards and alerting
- **Service Discovery** - Automatic service registration with Traefik

## Color Palette

- Primary Blue: `#0db7ed` (Docker blue)
- Secondary Blue: `#086dd7`
- Dark Blue: `#004d7a`
- Background gradients using these colors

### Infrastructure
- Docker & Docker Compose
- Nginx (web server)
- Traefik (reverse proxy)
- Prometheus (monitoring)
- Grafana (visualization)

## License

This project is open source and available under the [MIT License](LICENSE).