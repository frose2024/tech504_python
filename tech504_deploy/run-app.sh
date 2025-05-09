#!/bin/bash


# Needs to cd into the app folder
echo "Going to app folder"
cd ~/test-app/app

# Set the DB-host variable
echo "Setting DB-host variable"
export DB_HOST=mongodb://10.198.0.19:27017/posts

# Run the app with pm2
echo "Running app with pm2"
pm2 stop all || true
pm2 delete all || true

pm2 start app.js --name sparta_app
pm2 save

echo "Enabling PM2 startup on boot"
sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u $USER --hp $HOME

