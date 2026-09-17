def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):
    new_text = ""
    for char in word:
        if char.lower() in ["a","e","i","o","u"]:
            new_text += ""
        else:
            new_text += char

    return new_text

if __name__ == "__main__":
    main()



