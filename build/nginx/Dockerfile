FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
COPY ../../local_run/cardei_cert_chain.crt /etc/ssl/
COPY ../../local_run/cardei.key /etc/ssl/

#CMD sleep 10000
