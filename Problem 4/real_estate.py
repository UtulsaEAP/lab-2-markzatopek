
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    change = current_price - last_month_price
    mortgage_price = (current_price * 0.051) / 12.0
    
    print(f"This house is ${current_price}. The change is ${change} since last month.")
    print(f"The estimated monthly mortgage is ${mortgage_price:.2f}.")
    
if __name__ == "__main__":
    real_estate()