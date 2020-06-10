FROM python:3.5.2

WORKDIR /register

ADD . /register

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV NAME register

CMD ["python","src/Controller.py"]