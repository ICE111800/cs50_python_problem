def main():
    answer = input("What is the Answer to the Great Question of Life," \
    " the Universe, and Everything? ").strip().upper()
    print(Judgment_Answer(answer))

def Judgment_Answer(answer):
    word_1 = "forty-two".strip().upper()
    word_2 = "forty two".strip().upper()

    if answer == "42":
        return "Yes"
    elif answer == word_1:
        return "Yes"
    elif answer == word_2:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    main()