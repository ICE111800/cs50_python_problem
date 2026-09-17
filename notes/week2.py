# ==========================================
# 1. 重複執行與 While 迴圈 (While Loops)
# ==========================================

# --- 基礎重複 (笨方法) ---
print("meow")
print("meow")
print("meow")


# --- While 迴圈第一種寫法 ---
i = 3
while i != 0:
    print("meow")
    i = i - 1


# --- While 迴圈第二種寫法 ---
i = 1
while i < 3:
    print("meow")
    i = i + 1
    # 註：Python 沒有 ++ 遞增運算子，通常使用 i += 1


# ==========================================
# 2. For 迴圈與字串技巧 (For Loops & Strings)
# ==========================================

# --- 走訪 List ---
for i in [0, 1, 2]:
    print("meow")


# --- 更好的寫法 (使用 range) ---
for i in range(3):
    print("meow")


# --- Pythonic 寫法：用底線 _ 代表不會被用到的變數 ---
for _ in range(3):
    print("meow")


# --- 字串相乘技巧 ---
# print("meow" * 3)         # 有點小問題 (黏在一起)
# print("meow\n" * 3)       # 改進但最後會多一個空行
print("meow\n" * 3, end="")  # 完美改進：沒有多餘空行


# ==========================================
# 3. 互動輸入與錯誤防範 (User Input Validation)
# ==========================================

# --- 範例一：使用 continue 與 break ---
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue  # 繼續留在當前循環中
    else:
        break  # 跳出最近開始的循環


# --- 範例二：確保輸入大於 0 的常見寫法 ---
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# --- 範例三：將防呆機制封裝進 Function ---
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break  # 跳出最近循環
    return n  # 返回 n 值


def meow(n):
    for _ in range(n):
        print("meow")


# main()  # 執行主程式


# ==========================================
# 4. 列表 (Lists)
# ==========================================

# --- 基礎用法 ---
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])


# --- 更好的做法 (for-in 走訪) ---
# 說明：Python 會自動依序將元素賦值給 student 變數
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

# 不建議這樣寫，變數命名用底線會變得很晦澀
# for _ in students:
#     print(_)


# --- 結合 len() 取得索引與內容 ---
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):  # len() 回傳列表總數給 range
    # print(students[i])
    # print(i, students[i])
    print(i + 1, students[i])  # 優化：印出名次樣式


# ==========================================
# 5. 字典 (Dictionaries)
# ==========================================
# 說明：字典允許用實際的單詞作為 Key (索引) 來訪問 Value

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


# --- 動態印出 Key 與 Value ---
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# 這樣寫只會看到所有的 key
# for student in students:
#     print(student)

# 同時取得 key 與 value
for student in students:
    print(student, students[student], sep=", ")


# ==========================================
# 6. 結構化資料：Dict in List (物件清單)
# ==========================================
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None,
    },  # None 是特殊關鍵字，明確表示沒有值 (比空字串 "" 更好)
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


# ==========================================
# 7. 圖形列印練習：直行、橫列與矩形
# ==========================================

# --- 基礎直行 ---
for _ in range(3):
    print("#")


# --- 使用函式印出直行 (版本一) ---
def main_column_1():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


# --- 使用函式印出直行 (版本二：字串乘法) ---
def main_column_2():
    print_column_fast(3)


def print_column_fast(height):
    print("#\n" * height, end="")


# --- 使用函式印出橫列 ---
def main_row():
    print_row(4)


def print_row(width):
    print("?" * width)


# --- 巢狀迴圈印出正方形 (版本一) ---
def main_square_1():
    print_square_1(3)


def print_square_1(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


# --- 函式組合印出正方形 (版本二：更簡潔) ---
def main_square_2():
    print_square_2(3)


def print_square_2(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


# main_square_2()  # 測試呼叫