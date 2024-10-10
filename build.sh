#!/bin/bash

# Install Rust and Cargo
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env

# Install necessary build tools for compiling native extensions
apt-get update && apt-get install -y build-essential pkg-config libssl-dev

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
