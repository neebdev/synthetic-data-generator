#!/bin/bash

# Start Ollama in the background
/bin/ollama serve &
# Record Process ID
pid=$!

# Pause for Ollama to start
sleep 5

# Extract model name from MODEL variable (removing quotes if present)
MODEL_NAME=$(echo $MODEL | tr -d '"')

# Verificar que MODEL_NAME tenga un valor
if [ -z "$MODEL_NAME" ]; then
    echo "❌ No model specified in MODEL environment variable"
else
    # Check if model exists
    if ollama list | grep -q "$MODEL_NAME"; then
        echo "🟢 Model ($MODEL_NAME) already installed"
        touch /tmp/ollama_ready
    else
        echo "🔴 Retrieving model ($MODEL_NAME)..."
        # Intentar descargar el modelo sin crear el archivo hasta estar seguros
        if ollama pull "$MODEL_NAME" 2>/dev/null && ollama list | grep -q "$MODEL_NAME"; then
            echo "🟢 Model download complete!"
            touch /tmp/ollama_ready
        else
            echo "❌ Error downloading model ($MODEL_NAME)"
        fi
    fi
fi

# Wait for Ollama process to finish
wait $pid 