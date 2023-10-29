#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root or with sudo."
  exit 1
fi

# Update the package information using apt
apt update

# Upgrade installed packages (with -y to automatically answer yes to prompts)
apt upgrade -y 
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa
apt install python3.11 -y
apt install python3-pip -y
apt install python3-numpy
apt install python3-matplotlib

apt install gcc -y

# Check if the installation was successful
if [ $? -eq 0 ]; then
  echo "Packages and software installed successfully."
else
  echo "Some installations or updates failed. Please check for errors."
  exit 1
fi