FROM python:3

COPY ynab-updater ynab-updater
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD  ["python3", "ynab-updater/main.py"]