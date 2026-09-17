# ==========================================
# 1. 常見錯誤類型 (Exceptions)
# ==========================================

# --- 語法錯誤 (SyntaxError) ---
# 特點：程式執行前就會被檢查出來，通常是拼寫或符號漏掉
# SyntaxError: unterminated string literal
"""
print("hello, world)
"""



# --- 數值錯誤 (ValueError) ---
# 特點：型態正確，但內容無法被轉換或處理
# ValueError: invalid literal for int() with base 10: 'yi'
x = int(input("What's x? "))
print(f"x is {x}")


# ==========================================
# 2. Try-Except 基礎概念
# ==========================================
# 說明：try 用來捕捉可能發生錯誤的程式碼，except 用來處理特定錯誤 (不包含 SyntaxError)

# 範例：
try:
    x = int(input("What's x? "))
    print(f"x is {x}")  # <--- 這行在 try 區塊裡面
except ValueError:  # 當輸入不是數字時要執行的動作
    print("x is not an integer")

# 【思考點】：能一次性抓全部錯誤嗎？有何好處或壞處？
# 通常不建議盲目捕捉所有錯誤，應該根據經驗與情境去捕捉特定的預期錯誤。


# ==========================================
# 3. 變數範圍與 NameError 陷阱
# ==========================================

# --- 錯誤示範 ---
try:
    x = int(input("What's x? "))  # <--- 只有這行在 try 裡面
except ValueError:
    print("x is not an integer")

print(f"x is {x}")  # <--- 這行在 try 外部
#
# 【原因解析】：
# 當輸入 "cat" 時，int() 失敗引發 ValueError，程式直接跳進 except，
# 導致 x 根本沒有被建立 (not defined)。
# 當 try-except 結束後，外部的 print 尋找變數 x 卻找不到，因而拋出 NameError。


# ==========================================
# 4. 解決 NameError 的三種常見方法
# ==========================================

# --- 解決辦法一：使用 else 區塊 ---
# 說明：一旦 try 執行成功沒有報錯，就會執行 else 區塊
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


# --- 解決辦法二：結合 while True 與 else 迴圈 ---
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


# --- 解決辦法三：將 break 直接寫在 try 裡面 ---
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


# ==========================================
# 5. 封裝成函式 (Function) 的四種演進版本
# ==========================================

# --- 版本一：使用 else 與 break ---
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


# --- 版本二：使用 return 代替 break ---
# 說明：return 不僅能跳出迴圈，還能直接把值傳回給呼叫方
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x


# --- 版本三：更精簡的寫法 ---
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")


# --- 版本四：最精簡的寫法 (見仁見智，簡潔但可能較難閱讀) ---
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


# ==========================================
# 6. 使用 pass 略過錯誤訊息
# ==========================================
# 說明：pass 用於「想捕捉異常，但不想對它做任何額外操作 (例如不印出警告訊息)」的情境


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


# ==========================================
# 7. 提升函式的複用性 (Reusability)
# ==========================================
# 說明：透過帶入 prompt 參數，讓 get_int() 不再寫死固定的提問文字，
# 提升 Caller (調用者) 與 Callee (被調用者) 的彈性。


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()

# 註：關於 raise 主動拋出錯誤，將會在後續的課程中介紹！