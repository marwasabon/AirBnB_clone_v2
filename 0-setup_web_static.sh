#!/usr/bin/env bash
# this script is used to configuer the bnb static task
apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
cat << EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

#echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Nginx Server Configuration.
DR="/data/web_static"
DEST="/etc/nginx"
Static="/var/www/html"
echo "server  {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name localhost;
	add_header X-Served-By $HOSTNAME;
        error_page 404 /page_not_found.html;
        root $Static;

        location / {
                index index.nginx-debian.html index.html index.html;
        }

        location /hbnb_static/ {
                alias $DR/current/;
        }

}" > "$DEST/sites-available/default"
service nginx restart
