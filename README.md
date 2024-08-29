# EUR to BRL CRON script
Based on [exchangerate-api](https://www.exchangerate-api.com/docs/overview)

    0 7 * * * /usr/bin/python3 /<path>/eur.py >> /<path>/eur.txt 2>&1

## Requirements

    pip3 install requests python-dotenv

## Running

    python3 eur.py
