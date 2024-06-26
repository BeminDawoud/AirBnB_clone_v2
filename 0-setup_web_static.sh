#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get update 
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/
echo "Holberton School" >> /data/web_static/releases/test/index.html
if [ -e "/data/web_static/current" ]; then
	sudo rm /data/web_static/current
else
	sudo ln -s -n /data/web_static/releases/test/ /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location \/hbnb_static{\n\talias \/data\/web_static\/current\/;\n}' /etc/nginx/sites-available/default
service nginx restart
