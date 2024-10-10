#!/bin/bash
# This script installs Rust, Cargo, Python dependencies, and other tools

# Update the system package index (for Ubuntu/Debian)
sudo apt update


# Install Python and pip if not available
sudo apt-get install -y python3 python3-pip

# Verify Python and pip installation
python3 --version
pip3 --version

# Install Rust and Cargo (official Rust installer)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Source Cargo environment (make Cargo available immediately in this script)
source $HOME/.cargo/env

# Verify Rust and Cargo installation
rustc --version
cargo --version

# Install Python dependencies
pip3 install fastapi==0.101.0
pip3 install uvicorn==0.23.0
pip3 install sqlalchemy==1.4.48
pip3 install psycopg2-binary==2.9.6
pip3 install pydantic==1.10.9
pip3 install fastapi-jwt-auth==0.4.0
pip3 install python-multipart==0.0.6
pip3 install pillow==9.4.0
pip3 install web3
pip3 install aiofiles==0.8.0
pip3 install python-dotenv==1.0.0
pip3 install requests==2.28.1
pip3 install 'eth-utils>=2.1.0'
pip3 install gunicorn==20.1.0
pip3 install pysui
pip3 install maturin

gunicorn --version
# Confirm the installations
pip3 freeze
