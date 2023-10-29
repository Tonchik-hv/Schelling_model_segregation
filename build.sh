#!/usr/bin/env bash
echo "Starting build the project"

if ! command -v make &> /dev/null; then
	echo "Installing make..."
	sudo apt-get update
	sudo apt-get install -y make
fi

echo "Running make..."
make

if [ $? -eq 0 ]; then
	echo "Build process completed successfully."
else
	echo "Error: Build process encountered an error."
fi
