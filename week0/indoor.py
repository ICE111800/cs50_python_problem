word = input("Enter text: ")

if word.isupper() == True:
    print(f"{word}".lower())
elif word.islower() == True:
    print(f"{word}".upper())
else:
    print(f"{word}")