

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
    
    company = input().strip()

    if " " in company:
        return

    for name, ticker in COMPANIES.items():
        if company.lower() == name.lower():
            print(STOCKS[ticker])
            return


    print("Unknown company")



if __name__ == "__main__":
    tiker()

