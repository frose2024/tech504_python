#!/bin/bash
exec > /var/log/startup-script.log 2>&1
set -e

export DB_HOST=mongodb://10.198.0.15:27017/posts


echo "Updating any packages"
# Update packages. 
sudo apt update -y

echo "Installing packages"
# Install upgrade packages
sudo apt upgrade -y

echo "Downloading app code from repo"
# Download zipped app code from repo using curl command
curl -L -o nodejs20-sparta-test-app.zip https://raw.githubusercontent.com/frose2024/tech504_python/main/test_app/nodejs20-sparta-test-app.zip

echo "Installing unzip package"
# Install unzip package
sudo apt install unzip -y

echo "Making directories for app code"
# Make directory for test-app code
mkdir -p ~/test-app
mkdir -p ~/temp-dir

echo "Unzipping compressed app file"
# Unzip compressed app file
unzip nodejs20-sparta-test-app.zip -d ~/temp-dir

echo "Moving app content to constructed directory"
# Moving the contents of the test-app file (without the annoying sub-dreictory nonsense)
mv ~/temp-dir/nodejs20-sparta-test-app/* ~/test-app

echo "Deleting redudant directories"
# Clean up after myself
rm -r ~/temp-dir
rm nodejs20-sparta-test-app.zip

echo "Downloading nginx"
# Download + install + run nginx
sudo apt install nginx -y

echo "Altering nginx config file"
# Use sed to alter the try_file line in the sites-available/default file, inserting a proxy pass instead. 
sudo sed -i.bak 's|try_files \$uri \$uri/ =404;|proxy_pass http://localhost:3000;|' /etc/nginx/sites-available/default

echo "Restarting nginx so config changes are applied"
# Restart nginx so that the config changes work
sudo systemctl restart nginx

echo "Downloading correct version of node"
# Get the script to dowload + install the right version of nodejs
sudo bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -"

echo "Installing node"
# Download + install nodejs20
sudo apt install nodejs -y

echo "Navigating to test-app folder"
# Navigate to app folder
cd ~/test-app/app

echo "Installing node app"
# Install node app
npm install

echo "Installing pm2"
# Install pm2 globally
sudo npm install pm2@latest -g

echo "Cleaning up old pm2 processes"
# Stop and delete any old pm2 processes
pm2 stop all || true
pm2 delete all || true

echo "Starting the app"
# Start the app in the background with a clear name
pm2 start app.js --name sparta_app
pm2 save

echo "Enabling PM2 startup on boot"
sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u $USER --hp $HOME
