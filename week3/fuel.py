def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            Fuel_Percentage(fraction)
            break
        except (ValueError,ZeroDivisionError):
            pass
    
def Fuel_Percentage(fraction):
    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError

    x = int(parts[0])
    y = int(parts[1])

    if x < 0 or x > y or y == 0:
        raise ValueError

    result = round(((x / y) * 100))

    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result}%")

if __name__ == "__main__":
    main()