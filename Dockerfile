FROM python:3.5.2-alpine
ADD . /code
WORKDIR /code
RUN export CFLAGS=-Qunused-arguments
RUN export CPPFLAGS=-Qunused-arguments
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","api/app.py"]