# EUR to BRL CRON script
Based on [exchangerate-api](https://www.exchangerate-api.com/docs/overview)

    GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/BRL

    0 8 * * * /usr/bin/python3 /path/to/your/fetch_exchange_rate.py >> /path/to/your/logfile.log 2>&1

## Requirements

    pip3 install requests python-dotenv

## Running

    python3 eur.py
