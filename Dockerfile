FROM python:3.5.2-alpine
ADD . /code
WORKDIR /code
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN export CFLAGS=-Qunused-arguments
RUN export CPPFLAGS=-Qunused-arguments
RUN pip3.5 install -r requirements.txt
CMD ["python","api/app.py"]