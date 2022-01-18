FROM python:3.9

EXPOSE 80

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./api /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]