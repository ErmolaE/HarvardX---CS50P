import sys
import requests

def main():
    amount = get_amount()
    price = get_price()
    total = amount*price
    print(f"${total:,.4f}")

def get_amount():
    try:
        amount = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return amount

def get_price():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        price = r["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        pass
    return price

if __name__ == "__main__":
    main()