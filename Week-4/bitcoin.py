import requests
import sys

if len(sys.argv) == 2:
    try:
        if isinstance(float(sys.argv[1]), float):
            demand = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")
    
try:
    price = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=871f55f2587b2f42f41b6246a60e091b12dc453ce776cca6510d000992a724fd")
    price = float(price.json()["data"]["priceUsd"])
    amount = demand*price
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("Not Available")
    
    