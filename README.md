# Cardei Password Manager

The service is intended for reliable storage of account information. 
The information recorded in the database is encrypted with a unique key that can
only be accessed by the user. AES encryption algorithm is used. Only the 
user can view the decrypted data.
The user key is not stored anywhere on the server. If the user loses his
password to the service, his data can no longer be decrypted. The user can export
his data in json format.

### Steps to run a project on your system

    • Create a directory "local_run" in the root of the project
    • In the directory "local_run" create a file env.prod (the description of 
    the file will be below)

The env.prod file should have these values

    PYTHONUNBUFFERED=
    DJANGO_DEBUG=
    DJANGO_SECRET_KEY=
    CARDEI_ALLOWED_HOSTS=
    DB_ENGINE=
    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    DB_HOST=
    DB_PORT=
    DJANGO_SETTINGS_MODULE=
    DATABASE=
    CARDEI_CSRF_TRUSTED_ORIGINS=


The project is configured to work with a ssl certificate. If you do not have 
a ssl certificate, you must follow these steps

In the build/nginx directory, edit the nginx.conf file

        upstream cardei {
            server web:8000;
        }
        
        server {
            listen 80;
        
            access_log /opt/nginx-access.log;
            error_log /opt/nginx-error.log;
        
            location / {
                root /vue/dist/;
                index index.html index.htm;
                try_files $uri $uri/ /index.html;
            }
        
            location /api/ {
                proxy_pass http://cardei;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $host;
                proxy_redirect off;
            }
        
            location /admin/ {
                proxy_pass http://cardei;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $host;
                proxy_redirect off;
            }
        
            location /static/ {
                alias /files/web_static/;
            }
        
        }

Open file cardei_backend/cardei_backend/settings.py and remove the lines

        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        SECURE_SSL_REDIRECT = True
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True

#### The project can be run in docker using docker-compose.yml in the build directory