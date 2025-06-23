FROM alpine:3.22

RUN apk update && apk upgrade && apk add --no-cache \
        supervisor \
        nginx \
        musl-dev \
        build-base \
        gcc \
        linux-headers \
        python3-dev \
        python3 \
        && rm -rf /var/cache/apk/*

WORKDIR /app

COPY src/. .

COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/supervisord.conf /etc/supervisord.conf
COPY conf/uwsgi.ini /etc/uwsgi.ini

COPY conf/requirements.txt . 

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install -I --no-cache-dir -r requirements.txt

WORKDIR /

EXPOSE 1337

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"] 