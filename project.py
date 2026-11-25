from helpers import load_config, get_amount_rate, ceil

def main():
    config = load_config()
    parcel_config = config["parcel"]
    # User Inputs
    price = float(input("Price: "))
    currency = input("Currency: ")
    parcel_weight = float(input("Parcel Weight in Kg: "))
    
    # Main Logic
    # 1. convert parcel price to gel
    rate = get_amount_rate(currency)
    price_gel = convert_to_gel(price, rate)
    # 2. Calculate shipping cost for parcel
    shipping_cost = calc_shipping_cost(parcel_weight, parcel_config["shipping_cost_per_kg"])
    print(price_gel)
    print(shipping_cost)
    

def convert_to_gel(amount, rate):
    return round(amount * rate, 2)

def calc_shipping_cost(weight_kg, per_kg_rate_usd):
    usd_rate = get_amount_rate("usd")
    per_kg_gel = usd_rate * per_kg_rate_usd
    return round(ceil(weight_kg, 1) * per_kg_gel, 2)

if __name__ == "__main__":
    main()