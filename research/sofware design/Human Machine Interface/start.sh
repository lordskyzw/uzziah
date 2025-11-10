#!/bin/bash

# Exit if any variable is unset
set -u

# Function to start inference server
start_inference_server() {
  echo "Starting inference server..."
  inference server start &
  INFERENCE_PID=$!
  echo "Inference server PID: $INFERENCE_PID"
}

# Function to start Flask app
start_app() {
  echo "Starting Flask app..."
  python app.py &
  APP_PID=$!
  echo "App PID: $APP_PID"
}

# Function to restart a process if it stops
monitor_processes() {
  while true; do
    if ! kill -0 "$INFERENCE_PID" 2>/dev/null; then
      echo "Inference server crashed — restarting..."
      start_inference_server
    fi

    if ! kill -0 "$APP_PID" 2>/dev/null; then
      echo "App crashed — restarting..."
      start_app
    fi

    sleep 5
  done
}

# Main flow
start_inference_server
sleep 5  # give server time to initialize
start_app
monitor_processes
