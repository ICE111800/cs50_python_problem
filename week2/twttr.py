def main():
    text = input("Input: ")
    print(f"Output: {Omit_Vowels(text)}")

def Omit_Vowels(text):
    new_text = ""
    for char in text:
        if char.lower() in ["a","e","i","o","u"]:
            new_text += ""
        else:
            new_text += char

    return new_text

if __name__ == "__main__":
    main()