import emoji

def main():
    user_input = input("Input: ").strip()
    print(emoji.emojize(f"Output: {user_input}", language = "alias"))


if __name__ == "__main__":
    main()
