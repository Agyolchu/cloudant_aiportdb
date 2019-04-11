FROM python:3.5.2-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "api/app.py"]
