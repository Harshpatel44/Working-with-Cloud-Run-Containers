FROM python:3.5.2

WORKDIR /status

ADD . /status

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5002

ENV NAME status

CMD ["python","src/Controller.py"]