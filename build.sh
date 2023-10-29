#!/usr/bin/env bash
echo "Starting build the project"
run_script_with_sudo() {
	if [ -x "$1" ]; then
		echo "Executing $1 with sudo privileges..."
		sudo ./"$1"
		if [ $? -eq 0 ]; then
			echo "$1 executed successfully."
		else
			echo "Error: $1 encountered an error during execution."
			exit 1
		fi
	else
		echo "Error: $1 does not have execute permission."
		exit 1
	fi
}

if ! command -v make &> /dev/null; then
	echo "Installing make..."
	sudo apt-get update
	sudo apt-get install -y make
fi

run_script_with_sudo "prereqs.sh"
run_script_with_sudo "install_python.sh"
echo "Running make..."
make

if [ $? -eq 0 ]; then
	echo "Build process completed successfully."
else
	echo "Error: Build process encountered an error."
fi

