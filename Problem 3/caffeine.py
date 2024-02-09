import math

def half_life(mg, hour):
    return mg * math.pow(0.5, hour/6)

def caffeine():
    caffeine_mg = float(input())
    print(f"After 6 hours: {half_life(caffeine_mg, 6):.2f} mg")
    print(f"After 12 hours: {half_life(caffeine_mg, 12):.2f} mg")
    print(f"After 24 hours: {half_life(caffeine_mg, 24):.2f} mg")
    
    
if __name__ == "__main__":
    caffeine()