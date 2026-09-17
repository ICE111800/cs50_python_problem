def main():
    camelcase = input("camelCase: ").strip()
    print(f"snake_case: {Convert_Snake_Case(camelcase)}")

def Convert_Snake_Case(camelcase):
    new_string = ""
    for char in camelcase:
        if char.isupper():
            new_string += "_" + char.lower()
        else:
            new_string += char

    return new_string

if __name__ == "__main__":
    main()
