#!/bin/bash

# Update
echo "Retrieving update files"
sudo env DEBIAN_FRONTEND=noninteractive NEEDRESTART_MODE=a apt-get update

# Upgrade
echo "Installing update files"
sudo env DEBIAN_FRONTEND=noninteractive NEEDRESTART_MODE=a apt-get upgrade -y

# Install mongodb 7.0.6

# Installing dependencies of mongogb
echo "Installing mongoDB dependencies"
sudo env DEBIAN_FRONTEND=noninteractive NEEDRESTART_MODE=a apt-get install gnupg curl

# Import mongodb public GPG key
echo "Importing mongoDB public GPG key"
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

# Creates the file list for Ubuntu 22.04
echo "Creating file list of required packages for mongoDB"
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# Making sure that the packages needed from above command are updated
echo "Updating the packages as needed by above command"
sudo apt-get update

# Install the mongoDB packages for the correct version that we need
echo "installing mongoDB packages"
sudo env DEBIAN_FRONTEND=noninteractive NEEDRESTART_MODE=a apt-get install -y \
   mongodb-org=7.0.6 \
   mongodb-org-database=7.0.6 \
   mongodb-org-server=7.0.6 \
   mongodb-mongosh \
   mongodb-org-shell=7.0.6 \
   mongodb-org-mongos=7.0.6 \
   mongodb-org-tools=7.0.6 \
   mongodb-org-database-tools-extra=7.0.6


# Configure mongodb a teeny lil bit

# Change bindIp from 127.0.0.1 to 0.0.0.0
#   done using sed (I vaguely remember this from uni days. vageuly)
echo "Changing bindIP value"
sudo sed -i 's/bindIp: 127\.0\.0\.1/bindIp: 0.0.0.0/' /etc/mongod.conf

# Start mongodb using system process
echo "Starting mongoDB"
sudo systemctl start mongod

# Add it to the config file using sy
echo "Adding mongoDB to start up config file"
sudo systemctl enable mongod