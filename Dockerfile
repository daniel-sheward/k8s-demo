FROM python:3.8-buster

RUN pip install --no-cache-dir flask

COPY main.py .

CMD ["python", "main.py"]