FROM python:slim-stretch

RUN pip install flask
COPY ./url-shortener.py /
CMD "flask run -p 8080 /url-shortener.py"
