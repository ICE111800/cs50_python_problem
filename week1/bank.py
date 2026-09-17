def main():
    while True:
        greeeting = input("Greeting: ").strip().upper()
        if len(greeeting) > 0:
            print(Payment_Based_On_Greeting(greeeting))
            break
        else:
            pass

def Payment_Based_On_Greeting(greeting):
    word_1 = "hello".upper()

    if greeting.startswith(word_1):
        return "$0"
    elif greeting[0] == "H":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()