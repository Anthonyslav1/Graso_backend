#!/bin/bash
# This script installs Rust, Cargo, Python dependencies, and other tools

# Update the system package index (for Ubuntu/Debian)
sudo apt update

# Install Rust and Cargo (official Rust installer)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Source Cargo environment (make Cargo available immediately in this script)
source $HOME/.cargo/env

# Verify Rust and Cargo installation
rustc --version
cargo --version

# Install Python dependencies
pip install fastapi==0.101.0
pip install uvicorn==0.23.0
pip install sqlalchemy==1.4.48
pip install psycopg2-binary==2.9.6
pip install pydantic==1.10.9
pip install fastapi-jwt-auth==0.4.0
pip install python-multipart==0.0.6
pip install pillow==9.4.0
pip install web3
pip install aiofiles==0.8.0
pip install python-dotenv==1.0.0
pip install requests==2.28.1
pip install 'eth-utils>=2.1.0'
pip install gunicorn==20.1.0
pip install pysui==0.70.0
pip install maturin

# Confirm the installations
pip freeze

