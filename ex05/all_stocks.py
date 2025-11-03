import sys

def all_stocks():

    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }


    if len(sys.argv) != 2:
        return

    query = sys.argv[1].strip()


    if ",," in query or ", ," in query:
        return

    parts = query.split(",")

    for part in parts:
        name = part.strip()

        if not name:  
            return

        low = name.lower()

        for company, ticker in COMPANIES.items():
            if company.lower() == low:
                print(f"{company} stock price is {STOCKS[ticker]}")
                break
        else:
            flag = False
            for company, ticker in COMPANIES.items():
                if ticker.lower() == low:
                    print(f"{ticker} is a ticker symbol for {company}")
                    flag = True
                    break

            if not flag:
                print(f"{name} is an unknown company or an unknown ticker symbol")


if __name__ == "__main__":
    all_stocks()


