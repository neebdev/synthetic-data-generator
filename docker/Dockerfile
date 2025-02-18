# Use Python slim image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Create and set working directory
WORKDIR /app

# Create non-root user first
RUN useradd -m -u 1000 appuser

# Install system dependencies including build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    cmake \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pdm
RUN pip install --no-cache-dir pdm

# Copy project files and set permissions
COPY . .
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app

# Switch to non-root user
USER appuser

# Install dependencies in a virtual environment
RUN pdm install --prod --frozen-lockfile

# Expose Gradio port
EXPOSE 7860

# Start command using pdm run to use the virtual environment
CMD ["pdm", "run", "python", "-m", "synthetic_dataset_generator"] 