import datetime
import json
import random
import os

# Python script to generate the n - number of purchases.
# -> YYYY-MM-DD Change this date to your desired input date

Total_Purchases = 15000
# Purchase_Date = "2023-09-24"                                      # If you want a specific date
Purchase_Date = datetime.datetime.today().strftime("%Y-%m-%d")      # generates today's date

# generate Items Qty
# assume most people orders (1) (2) (3) in Maximum times
# Generate a random number with a preference for preferred numbers
# weights means 1 appears four times more likely than 2, 3.
# Menu_Items: We assume above patterns will the Items ordered, Quantity will be generated randomly.
# Random UUID as StoreID
# Random alphanumeric OrderID

Preferred_Numbers = [1, 2, 3, 4]
Random_Number = random.choices(Preferred_Numbers, weights=[4, 2, 2, 2], k=3)
x, y, z = max(Random_Number), Random_Number[1], min(Random_Number)
Menu_Items = [f'{x}-burgers, {y}-fries, {z}-coke', f'{x}-burgers, {y}-fries', f'{z}-fries, {z}-coke', f'{x}-burgers']


def generate_purchase_history():
    # Generate a random Store Address
    cities = {'Texas': ['San Marcos', 'Austin']}
    state = random.choice(list(cities.keys()))
    city = random.choice(cities[state])
    zip_codes = {'San Marcos': [78666, 78667, 78668], 'Austin': [78717, 78718, 78719]}
    zip_num = random.choice(zip_codes[city])

    # Create a new purchase history entries
    purchases = {
        "StoreID": random.choice([f'A{zip_num}', f'B{zip_num}']),
        "OrderID": ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(14)),
        "Items": random.choice(Menu_Items),
        "PurchaseDate": Purchase_Date,
        "City": city,
        "State": state,
        "ZipCode": zip_num,
        "Price": round(random.uniform(5, 20), 2),
        "PurchaseType": random.choice(["In-Store", "App"]),
        "PaymentMode": random.choice(["Cash", "Credit/Debit"])
    }

    # return generated purchases
    return purchases


if __name__ == "__main__":

    file_path = os.path.join("..", "customer-purchases-in-json", f'purchases-{Purchase_Date}.json')
    with open(file_path, 'w') as fp:
        purchase_list = []
        for each_purchase in range(Total_Purchases):
            purchase = generate_purchase_history()
            purchase_list.append(purchase)

        fp.write(json.dumps(purchase_list, indent=4))

