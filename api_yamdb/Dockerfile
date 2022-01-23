FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install -r /app/requirements.txt --no-cache-dir
CMD ["gunicorn", "api_yamdb.wsgi", "--bind", "0:8000"]
LABEL author='Dmitry Nekrasov' version=1
