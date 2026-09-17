def main():
    word = input("Enter text: ")
    print(convert(word))


def convert(word):
    new_word = word.replace(":)", "🙂").replace(":(", "🙁")
    return new_word

if __name__ == "__main__":
    main()