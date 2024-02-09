
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    product = num1 * num2 * num3 * num4
    average = (num1 + num2 + num3 + num4) / 4.0
    
    print(f"{int(round(product, 0))} {int(round(product, 0))}")
    print(f"{product:.3f} {average:.3f}")
    
if __name__ == "__main__":
    simple_stats()