FROM python:3.8

RUN pip freeze > requirements.txt

ADD alerting/alert_system.py /
ADD requirements.txt /
ADD data/data.csv /


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD ["python","alert_system.py"]