from random import randint
import sys

def main():
    # 取得遊戲難度（Level）的迴圈
    while True:
        try:
            # 【精準防禦】：只用 try 包覆可能發生 EOFError (Ctrl + D) 的 input() 這一行
            level = input("Level: ").strip()
        except EOFError:
            # 如果使用者中斷輸入，優雅地離開程式
            sys.exit("\nExiting program.")

        # 檢查輸入是否為「正整數」（必須是數字且大於 0） 
        if level.isdigit() and int(level) > 0:
            break

    # 將合法的 level 轉為整數，並在 1 到 n 之間隨機產生一個目標數字
    int_level = int(level)
    random_num = randint(1, int_level)

    # 猜數字（Guess）的核心遊戲迴圈
    while True:
        try:
            # 同樣精準包覆 input()，防範猜數字時的突發中斷
            guess = input("Guess: ").strip()
        except EOFError:
            sys.exit("\nExiting program.")

        # 檢查使用者的猜測是否為合法的正整數
        if guess.isdigit() and int(guess) > 0:
            int_guess = int(guess)

            # 比對大小並給予對應的提示
            if int_guess == random_num:
                print("Just right!")
                break # 猜對了，跳出遊戲迴圈
            elif int_guess < random_num:
                print("Too small!")
            elif int_guess > random_num:
                print("Too large!")
        
if __name__ == "__main__":
    main()
        