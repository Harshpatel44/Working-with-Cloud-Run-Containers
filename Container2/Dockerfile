FROM python:3.5.2

WORKDIR /login

ADD . /login

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5001

ENV NAME login

CMD ["python","src/Controller.py"]