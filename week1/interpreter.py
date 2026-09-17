def main():
    while True:
        expression = input("Expression: ")
        x, y, z = expression.split(" ")
        if y in ["+", "-", "*", "/"]:
            print(f"{Calculation(x, y, z):.1f}")
            break
        else:
            pass
            

def Calculation(x, y, z):
    x = float(x)
    z = float(z)
    if y == "+":
        return x + z
    elif y == "-" :
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

if __name__ == "__main__":
    main()