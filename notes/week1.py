# ==========================================
# 條件判斷式 (Conditionals: if, elif, else)
# 常用運算子：>、>=、<、<=、==、!=
# ==========================================


# --- 第一版：多個 if 獨立判斷 ---
# 缺點：即使前面的條件已經成立，電腦還是會把所有 if 都檢查一遍
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")


# --- 第二版：使用 elif ---
# 優點：一旦某個條件達成就會直接結束，不用像第一版那樣全部問完
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")


# --- 第三版：使用 else ---
# 好處：比第二版少問一個問題，從流程圖上看複雜度更低
# (註：原程式碼倒數第二行語法筆誤應為 `else:` 而非 `else x == y:`)
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# ==========================================
# 邏輯運算子：or
# ==========================================

# --- 初步寫法 ---
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# --- 優化寫法 ---
# 養成思考習慣：Code 能不能更簡潔？
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# ==========================================
# 邏輯運算子：and 與範圍縮寫
# ==========================================
score = int(input("Score: "))

# --- 第一版：傳統寫法 ---
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# ...


# --- 第二版：數學範圍串接 (更直覺) ---
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# ...


# --- 第三版：簡化版 (更精簡) ---
# 好在哪？因為前面的條件已經過濾掉更高的分數，這裡只需要檢查下限即可
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# ==========================================
# 餘數運算 (%): 判斷奇偶數
# ==========================================
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# ==========================================
# 布林值與 Pythonic 風格寫法
# ==========================================


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# --- 傳統寫法 ---
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# --- 更 Python 風格的寫法 ---
def is_even(n):
    return True if n % 2 == 0 else False


# --- 最精簡的 Pythonic 寫法 ---
def is_even(n):
    return n % 2 == 0


main()


# ==========================================
# 模式比對 (match 語法，類似其他語言的 switch-case)
# ==========================================

# --- 傳統 if-elif 寫法 ---
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


# --- match 語法 (基礎版) ---
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  # _ 表示所有未被處理的 case (預設選項)
        print("Who?")


# --- match 語法 (精簡管線版 |) ---
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  # _ 表示所有未被處理的 case
        print("Who?")