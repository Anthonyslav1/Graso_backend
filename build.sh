#!/bin/bash

# Install Rust and Cargo
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env

# Install Python dependencies
pip install -r requirements.txt
