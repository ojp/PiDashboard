FROM resin/rpi-raspbian:wheezy-2015-01-15

# Install Python.
RUN apt-get update && apt-get install -y python
RUN apt-get install -y python-pygame

# Configure timezone and locale
RUN echo "Europe/Amsterdam" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

ADD . /app

CMD ["python", "/app/minidash.py"]