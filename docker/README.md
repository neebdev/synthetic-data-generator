# Docker Configuration Guide

The application can be run with different configurations using Docker Compose:

- `docker-compose.yml`: Core application
- `docker/ollama/compose.yml`: Ollama service for local LLM inference
- `docker/argilla/compose.yml`: Argilla service for data curation

## Ollama Integration

The `MODEL` variable in your `.env` file determines which model Ollama will download and use. For example:
```env
MODEL=llama3.2:1b
```

- Ollama will automatically download and set up the specified model
- No manual commands or downloads are needed


## Setup Options

### Full Setup (App + Ollama + Argilla)
```bash
# Keep all sections uncommented in .env
docker compose -f docker-compose.yml -f docker/ollama/compose.yml -f docker/argilla/compose.yml build
docker compose -f docker-compose.yml -f docker/ollama/compose.yml -f docker/argilla/compose.yml up -d
```

### App + Ollama
```bash
# Comment out ARGILLA section in .env
docker compose -f docker-compose.yml -f docker/ollama/compose.yml build
docker compose -f docker-compose.yml -f docker/ollama/compose.yml up -d
```

### App + Argilla
```bash
# Comment out OLLAMA section in .env
docker compose -f docker-compose.yml -f docker/argilla/compose.yml build
docker compose -f docker-compose.yml -f docker/argilla/compose.yml up -d
```

### App Only
```bash
# Comment out both OLLAMA and ARGILLA sections in .env
docker compose -f docker-compose.yml build
docker compose -f docker-compose.yml up -d
```

## Managing Services

Services are built separately but are linked together. If you already have some services built and want to add another:

1. You don't need to rebuild existing services
2. Just build the new service
3. Stop everything with `down` and start again with `up`

For example, if you have App + Ollama and want to add Argilla:
```bash
docker compose -f docker/argilla/compose.yml build  # only build Argilla
docker compose -f docker-compose.yml -f docker/ollama/compose.yml -f docker/argilla/compose.yml down
docker compose -f docker-compose.yml -f docker/ollama/compose.yml -f docker/argilla/compose.yml up -d
```

Similarly, if you have built all services but want to run only some of them:
> **Important**: When running specific services, remember to comment out unused services in `.env` first

```bash
# No need to build again, just start the services you need
docker compose -f docker-compose.yml -f docker/ollama/compose.yml up -d  # start only App + Ollama
```

## Service URLs

Once running, access the services at:
- App: http://localhost:7860
- Argilla: http://localhost:6900 (if enabled)
- Ollama: http://localhost:11434 (if enabled)

> Note:  Services will be available after a few seconds while they initialize. Ollama models and Argilla datasets are persisted and available after restarts