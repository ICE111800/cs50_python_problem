"""
=============================================================================
📚 CS50 Python - 單位測試 (Unit Tests) 與 Pytest 完整複習筆記
=============================================================================
使用說明：
此檔案整合了你從手動測試、斷言 (assert)、例外處理、pytest 框架，
一直到專案資料夾結構設計的所有觀念與程式碼範例。
"""

# =============================================================================
# 一、 單位測試的概念與手動測試的演進
# =============================================================================

"""
1. 什麼是單位測試 (Unit Test)？
   - 單元測試是一種正式說法，指的是測試程序的各個「獨立單元」（通常指的是獨立函數）。
   - 目標：不依賴手動輸入，透過自動化流程來反覆運行、驗證程式是否正確。

2. 被測試的主函數 (以 square 為例)：
"""

def square(n):
    return n * n

# 早期手動測試的缺點：每次都必須手動傳入數字（如 x = 2, x = 3），
# 操作繁瑣且無法自動化。

# =============================================================================
# 二、 自建測試程式碼與 assert 斷言機制
# =============================================================================

"""
【第一版手動測試 (test2.py)】
把測試條件寫進 code 裡，雖然不用動手互動，但寫起來很冗長：
"""

def test_square_manual():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


"""
【使用 assert 斷言】
- assert 用來聲明某件事是真實的。
- 斷言成立：什麼事都不會發生（安靜地通過）。
- 斷言不成立：螢幕會拋出 AssertionError。
"""

def test_square_assert():
    assert square(2) == 4
    assert square(3) == 9


"""
【加上 try...except 捕捉 AssertionError】
雖然能自訂錯誤提示，但如果測試案例一多，程式碼會變得過於臃腫：
"""

def test_square_try_except():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


# =============================================================================
# 三、 使用 pytest 第三方測試框架
# =============================================================================

"""
1. Pytest 的優勢：
   - 透過「約定」幫你自動處理標準化操作（不需要自己寫 try、except、print）。
   - 安裝指令：pip install pytest
   - 執行指令：pytest filename.py

2. 最佳實踐：將測試拆分成多個獨立函數
   - 不要把所有測試擠在同一個函數裡。
   - 拆分成多個小測試（如 positive, negative, zero），即使其中一個失敗，
     其他測試也會繼續運行，提供更多除錯線索。
"""

import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


# =============================================================================
# 四、 測試例外狀況 (Testing Exceptions)
# =============================================================================

"""
如果主程式因為輸入錯誤型態（例如傳入字串 "cat" 而非數字）而拋出 TypeError，
我們該如何用 pytest 測試這種異常情況？

使用 `pytest.raises(預期發生的異常類型)`：
"""

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# =============================================================================
# 五、 避免副作用：讓函數可被測試 (Refactoring for Testability)
# =============================================================================

"""
【錯誤示範（有副作用的函數）：】
如果 hello 函數裡面直接 print，而不是用 return 返回結果：
    def hello(to="world"):
        print("hello,", to)
這樣使用 assert 會無法檢查返回值（因為返回值是 None）。

【正確示範（返回結果供測試）：】
最佳實踐是盡量避免在測試函數中產生副作用，讓函數擁有明確的輸入與輸出：
"""

def hello_refactored(to="world"):
    return f"hello, {to}"

def test_hello_default():
    assert hello_refactored() == "hello, world"

def test_hello_argument():
    assert hello_refactored("David") == "hello, David"


# =============================================================================
# 六、 專案資料夾結構與 pytest 批量測試
# =============================================================================

"""
【標準專案結構規範 (CS50 最佳實踐)】
1. 根目錄 (`cs50_python/`)：
   - 放被測試的主程式檔案，例如 `hello.py`。
   
2. 建立測試資料夾 (`test/`)：
   - 使用指令：mkdir test
   - 在裡面創建 `__init__.py`（可以空白，用來告訴 Python 這個資料夾是一個 package）。
   - 創建測試檔案，例如 `test/test_hello.py`。
   
3. 導入主程式的寫法：
   - 因為 `hello.py` 在根目錄，測試檔在 `test/` 內，導入時寫：
     `from hello import hello`

4. 執行批量測試：
   - 不用指定特定檔案，直接執行整個資料夾：
     `pytest test`
   - pytest 會自動搜尋該資料夾下的所有測試檔案並執行！
"""

print("========================================================")
print("這是單元測試與 Pytest 複習腳本，建議搭配終端機指令實作練習！")
print("========================================================")



"""
=============================================================================
📚 CS50 Python - 單位測試 (Unit Tests) 課程完整程式碼與筆記總結
=============================================================================
"""

# =============================================================================
# 1. 基礎被測試函數：square (平方函數)
# =============================================================================

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()


# =============================================================================
# 2. 第一版手動測試 (test2.py) - 嵌入 if 判斷式
# =============================================================================
"""
# 執行指令: python test2.py (正常無輸出)
"""

from test import square

def main_test1():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    # main_test1()
    pass


# =============================================================================
# 3. 引入 assert 斷言機制
# =============================================================================
"""
- assert 宣告某件事為真。成立沒事，不成立會直接噴出 AssertionError。
"""

from test import square

def test_square_assert():
    assert square(2) == 4
    assert square(3) == 9


# =============================================================================
# 4. 加上 try...except 捕捉 AssertionError 自訂錯誤訊息
# =============================================================================

from test import square

def test_square_try_except():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
        
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
        
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
        
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
        
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


# =============================================================================
# 5. 使用 Pytest 第三方測試框架與多個獨立測試函數
# =============================================================================
"""
- 安裝: pip install pytest
- 執行: pytest test2.py
- 優點: 不用寫多餘的 try、except、print，且即使其中一個失敗，其他測試也會繼續執行。
"""

from test import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


# =============================================================================
# 6. 測試例外狀況 (Testing Exceptions) - 使用 pytest.raises
# =============================================================================
"""
- 用來測試當傳入錯誤型態（如字串 "cat"）時，是否如預期拋出 TypeError。
- 執行: pytest test2.py
"""

import pytest
from test import square

# (前面正負數與 zero 測試省略...)

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# =============================================================================
# 7. 避免副作用：設計可被測試的 hello 函數
# =============================================================================
"""
【錯誤示範（有副作用）：】
def hello(to="world"):
    print("hello,", to)  # 只有 print，沒有 return，無法用 assert 檢查返回值。

【正確示範（具備明確返回值）：】
"""

def main_hello():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    # main_hello()
    pass


# =============================================================================
# 8. hello 函數的 Pytest 測試寫法
# =============================================================================

from test import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

# 也可以用迴圈測試多個參數
def test_argument_loop():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"


# =============================================================================
# 9. 專案資料夾結構與批量測試 (CS50 標準實踐)
# =============================================================================
"""
【步驟說明】
1. 在根目錄 (`cs50_python/`) 建立被測試的主程式，例如 `hello.py`：
   ------------------------------------------------------------
   def main():
       name = input("What's your name? ")
       print(hello(name))
       
   def hello(to="world"):
       return f"hello, {to}"

   if __name__ == "__main__":
       main()
   ------------------------------------------------------------

2. 建立測試資料夾與初始化檔案：
   - 指令: mkdir test
   - 在 test/ 裡面建立 `__init__.py`（告訴 Python 這是個 package）。
   - 在 test/ 裡面建立測試檔 `test_hello.py`：
     ----------------------------------------------------------
     from hello import hello  # 從根目錄導入主程式

     def test_default():
         assert hello() == "hello, world"

     def test_argument():    
         assert hello("David") == "hello, David"
     ----------------------------------------------------------

3. 執行整個測試資料夾：
   - 指令: pytest test
   - Pytest 會自動搜尋該資料夾下所有符合條件的測試檔案並執行！
"""