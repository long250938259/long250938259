FROM python:3.8-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

ENV environment development
EXPOSE 8000

#命令运行
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']