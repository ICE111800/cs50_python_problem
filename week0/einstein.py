def main():
    m = int(input("Enter weight in kilograms: "))
    print(f"{Energy_Conversion(m)}")

def Energy_Conversion(m):
    c = 300000000
    e = m * (c ** 2)
    return e

if __name__ == "__main__":
    main()
