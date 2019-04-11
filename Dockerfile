FROM python:3.5.2-alpine
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD ["python","api/app.py"]