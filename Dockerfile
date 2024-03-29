FROM debian

ENV PORT 5000
ENV NB_WORKERS 1

VOLUME /data

WORKDIR /usr/src/app

RUN apt update;\
	apt install -y python3 python3-pip;\
	python3 -m pip install flask gunicorn;
COPY ./url-shortener.py ./
CMD touch /data/urls.csv && gunicorn -w ${NB_WORKERS} -b 0.0.0.0:${PORT} url-shortener:app
