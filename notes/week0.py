"""
------------------------------------------------------
字串處理與輸入練習 (String Methods)
------------------------------------------------------
"""

# 1. 取得使用者輸入
name = input("What's your name? ")

# ------------------------------------------
# 2. 字串處理方法介紹
# ------------------------------------------

# 去除前後兩端的空白字符
name = name.strip()

# 將字串第一個字元大寫
name = name.capitalize()

# 將每個單詞的首字母大寫 (Title Case)
name = name.title()

# 【技巧】也可以串接方法（從左至右執行）：
name = name.strip().title()

# ------------------------------------------
# 3. 輸出方式比較
# ------------------------------------------

print("hello, " + name)
print("hello,", name)

# 建議使用 f-string，閱讀與維護最直覺
print(f"hello, {name}")

# 引號巢狀使用範例：
print('hello, "friend"')
print("hello, \"friend\"")

# ------------------------------------------
# 4. 字串分割 (Split)
# ------------------------------------------

# 以空白字元為分隔符號，把字串拆分成多個變數
# 例如輸入 "John Doe"，會分別指定給 first 與 last
first, last = name.split(" ")

print(f"hello, {first}")


# ==========================================
# 1. 互動模式 (Interactive Mode)
# ==========================================
# 在終端機 (Terminal) 輸入 python 後即可使用：
# >>> 1 + 1
# 2
# >>> print("hello, world")
# hello, world
# >>>


# ==========================================
# 2. 整數運算 (int)
# ==========================================

# --- 基礎觀念與第一版 ---
x = input("What's x? ")
y = input("What's y? ")
z = x + y  # 錯誤：此時為字串相接 (str)

z = int(x) + int(y)  # 正確：轉換為整數後相加
print(z)


# --- 第二版：較佳的寫法 ---
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)


# --- 第三版：單行寫法 (可讀性較差) ---
print(int(input("What's x? ")) + int(input("What's y? ")))


# ==========================================
# 3. 浮點數與格式化 (float)
# ==========================================

# --- 基本浮點數相加 ---
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y)


# --- 四捨五入 (round) ---
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(z)


# --- 千分位逗號格式化 ---
# 範例：999 + 1 = 1000 -> 顯示為 1,000
print(f"{z:,}")


# --- 除法運算 ---
# 範例：2 / 3 = 0.66666...
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(z)


# --- 指定小數點位數 (方法一：round) ---
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)
print(z)


# --- 指定小數點位數 (方法二：f-string 格式化) ---
# 範例：2 / 3 = 0.67
z = x / y
print(f"{z:.2f}")



# ==========================================
# 1. 函式初探 (def)
# ==========================================

# --- 第一版 ---
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)


# --- 第二版：帶有預設參數與引數 ---
# name 變數的值會被傳遞給 function 的 to 變數，預設值為 "world"
def hello(to="world"):
    print("hello,", to)


hello()  # 不帶參數，使用預設值 "world"
name = input("What's your name? ")
hello(name)  # 傳入 name 參數


# ==========================================
# 2. 標準的程式結構 (main function)
# ==========================================
# 說明：
# 如果把 def hello() 放後面、上面卻先呼叫它，Python 會報錯，因為它還沒讀到該函式。
# 但如果每次都把函式定義在最上方，程式邏輯就會變成「倒著寫」。
# 因此，更標準的做法是將「程式主體」包在 main() 裡面，最後再呼叫 main()。


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


# 執行主程式
main()


# ==========================================
# 3. 變數作用域錯誤示範 (Scope Error)
# ==========================================
# 說明：作用域 (Scope) 是指變數只在定義它的上下文中存在。
# 以下程式會報錯，因為 hello() 函式無法直接讀取 main() 裡面的 name 變數。

def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello,", name)  # 錯誤：name 在這裡未定義

main()


# ==========================================
# 4. 回傳值 (return)
# ==========================================
# 說明：return 可以把運算結果回傳給呼叫它的地方。


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n  # 也可以寫成 return n ** 2 或 return pow(n, 2)


main()
