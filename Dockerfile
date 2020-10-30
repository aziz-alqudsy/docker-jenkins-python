FROM python:3.7-slim

MAINTAINER yes.mail.me.here@gmail.com

COPY . /jenkins-demo

WORKDIR /jenkins-demo

RUN pip install -r requirements.txt -U

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null
