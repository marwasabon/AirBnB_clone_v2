#!/usr/bin/env bash
apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Nginx Server Configuration.
DR="/data/web_static"
DEST="/etc/nginx"
Static="/var/www/default"
echo "server  {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name localhost;
	add_header X-Served-By $HOSTNAME;
        error_page 404 /page_not_found.html;
        root $Static;

        location / {
                index index.html index.html;
        }

        location /hbnb_static/ {
                alias $DR/current/;
        }

}" > "$DEST/sites-available/default"
service nginx restart
