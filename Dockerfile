FROM python:3.5.2-alpine
ADD . /code
WORKDIR /code
RUN export CFLAGS=-Qunused-arguments
RUN export CPPFLAGS=-Qunused-arguments
RUN pip3.5 install -r requirements.txt
CMD ["python","api/app.py"]