import sys

def tiker():

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

    if(len(sys.argv) != 2):
        return

    query = sys.argv[1].strip()



    for name, ticker in COMPANIES.items():
        if query.lower() == ticker.lower():
            print(name, STOCKS[ticker])
            return

    print("Unknown ticker")

if __name__ == "__main__":
    tiker()