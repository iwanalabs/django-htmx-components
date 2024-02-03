#!/bin/bash
set -e

SERVER_ADDRESS=components

echo "Copying files to server"
scp ./init.sh ubuntu@$SERVER_ADDRESS:~/
scp ./config.sh ubuntu@$SERVER_ADDRESS:~/
