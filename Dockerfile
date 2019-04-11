FROM python:3.5.2-alpine
ADD . /code
WORKDIR /code
RUN apk update
RUN apk -U add build-base linux-headers build-essential libssl-dev libffi-dev mariadb-dev \
    gettext curl gcc musl-dev python3-dev libressl-dev perl
RUN apk add make automake gcc g++ subversion python3-dev
RUN export CFLAGS=-Qunused-arguments
RUN export CPPFLAGS=-Qunused-arguments
RUN pip3.5 install -r requirements.txt
CMD ["python","api/app.py"]