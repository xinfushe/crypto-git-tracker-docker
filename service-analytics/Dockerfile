FROM python:3.6.4

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install supervisord
RUN apt-get update && apt-get install -y supervisor

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# force celery to accept root inside docker
ENV C_FORCE_ROOT=1

# run supervisord
CMD ["/usr/bin/supervisord"]