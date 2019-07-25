FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 9406

ENTRYPOINT ["python3"]

CMD ["-m", "application", "--debug=False", "--host=0.0.0.0", "threaded=True"]
