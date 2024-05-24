#!/usr/bin/env bash

# Update your package lists for upgrades and new package installations.
sudo apt-get update

# Install necessary packages
sudo apt-get install -y software-properties-common wget xfonts-75dpi xfonts-base libxrender1

# Download the wkhtmltopdf package.
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb

# Install the wkhtmltopdf package.
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb

# Fix any missing dependencies with sudo apt-get install -f
sudo apt-get install -f

# Check version
wkhtmltopdf --version

# Remove the downloaded package.
rm wkhtmltox_0.12.6.1-2.jammy_amd64.deb
