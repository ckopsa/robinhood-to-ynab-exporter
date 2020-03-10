# Robinhood to YNAB Updater
Just some code to get your Robinhood transactions into YNAB.

# How To Run It
First extract your credentials from YNAB and Robinhood into `ynab-updater/credentials.py`.

```python
# ynab-updater/credentials.py

# Include Bearer (ex: Bearer #@#$@$@$)
robinhood_token = "INSERT_ROBINHOOD_TOKEN_HERE"

ynab_token = "INSERT_YNAB_TOKEN_HERE"
```
## YNAB
Follow the instructions [here](https://api.youneedabudget.com/) to get your API key.

## Robinhood
1. Login to Robinhood
1. Open Developer Tools
1. Navigate to the Network tab
1. Click on any of the network calls
1. Navigate to the Headers tab
1. Scroll down to "Request Headers"
1. Copy the value of "authorization" into the credentials file.


Then to run the updater do the following:
```shell script
pip install -r requirements.txt
python3 ynab-updater/main.py
```
OR
```shell script
docker image build -t ynab-updater:1.0 .
docker container run -it ynab-updater:1.0
```