FROM resin/rpi-raspbian:wheezy-2015-01-15

ENV TIMEZONE Europe/Amsterdam

# Install Python.
RUN apt-get update && apt-get install -y python
RUN apt-get install -y python-pygame


ADD . /app

CMD ["python", "/app/minidash.py"]