# =============================================================================
# 📚 CS50 Python - 集合 (Set)、全域變數 (Global)、常數 (Constants) 與類別應用總結複習
# =============================================================================
"""
使用說明:
此檔案包含完整的程式碼以及詳細的觀念註解，專門用來解答「為什麼要這樣寫」的疑惑。
"""

# =============================================================================
# 觀念一: 集合 (Set) 的特性與應用（自動去除重複元素）
# =============================================================================
"""
【觀念解說】
- `set`（集合）是一種不包含重複元素、無序的資料結構。
- 如果我們想要找出資料中所有「不重複」的項目（例如所有學生所屬的學院），
  傳統用 `list` 加上 `not in` 判斷雖然可行，但程式碼較冗長。
- 改用 `set` 之後，新增元素使用 `add()` 而非 `append()`，且 Python 會自動幫我們過濾重複值。
- 在 `set` 中尋找特定元素同樣可以使用 `in` 與 `not in` 進行高效檢查。
"""

# 傳統使用 list 尋找獨特學院的方法
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)


# 使用更簡潔的 set 集合來過濾重複元素
houses_set = set()
for student in students:
    houses_set.add(student["house"])

for house in sorted(houses_set):
    print(house)


# =============================================================================
# 觀念二: 全域變數 (Global Variable) 與 UnboundLocalError 陷阱
# =============================================================================
"""
【觀念解說】
- 定義在檔案頂部的變數通常被視為「全域變數」（在 Python 中嚴格來說是模組級別）。
- 函數內部可以「讀取/訪問」全域變數的值，但如果嘗試在函數內部「修改」它（例如 `balance += n`），
  Python 會預設該變數為「局部變數（Local Variable）」。
- 這會導致 `UnboundLocalError`（未綁定本地變數錯誤），因為 Python 發現你在賦值前就試圖引用它。
- 解決方法：必須在函數內部使用 `global 變數名稱` 關鍵字，明確告訴 Python 這不是局部變數，而是要修改全域變數。
- ⚠️ 工程師實務建議：全域變數容易讓程式碼變混亂，通常不建議在大型專案中隨意使用。
"""

balance = 0

def deposit(n: int) -> None:
    global balance
    balance += n

def withdraw(n: int) -> None:
    global balance
    balance -= n

def main_global_demo() -> None:
    global balance
    print("Balance (Global):", balance)
    deposit(100)
    withdraw(50)
    print("Balance (Global):", balance)

if __name__ == "__main__":
    main_global_demo()


# =============================================================================
# 觀念三: 透過物件導向 (OOP) 封裝狀態取代全域變數
# =============================================================================
"""
【觀念解說】
- 與其使用容易造成混亂的全域變數，物件導向（OOP）是更好的解法。
- 我們可以建立一個 `Account` 類別，將帳戶餘額封裝在類別內部作為實例變數（Instance Variable）。
- 習慣上將變數命名為 `_balance`（前方加底線），雖然 Python 不強制私有性，但這是一個給其他開發者的
  「視覺提示」，代表不應該從外部直接修改它，而應該透過類別中的方法來操作。
- 透過 `@property` 裝飾器可以安全的將方法包裝成屬性來唯讀訪問。
"""

class Account:
    def __init__(self) -> None:
        # 使用底線開頭表示內部變數（視覺上的私有提示）
        self._balance = 0

    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, n: int) -> None:
        self._balance += n

    def withdraw(self, n: int) -> None:
        self._balance -= n

def main_oop_demo() -> None:
    account = Account()
    print("Balance (OOP):", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance (OOP):", account.balance)

if __name__ == "__main__":
    main_oop_demo()


# =============================================================================
# 觀念四: 常數 (Constants) 的定義與規範
# =============================================================================
"""
【觀念解說】
- 在許多程式語言中有真正的「常數（Constants）」機制（賦值後無法更改），但 Python 沒有強制語法。
- Python 採用「約定俗成」的方式：如果某個變數不應該被修改，就把它的名字**全部改為大寫**（例如 `MEOWS`）。
- 這樣做可以避免把數值直接寫死在程式碼中（Magic Numbers），未來需要修改時只需在頂部或類別常數區調整即可。
- 類別中也可以定義「類常數（Class Constants）」，供類別內部的方法透過 `類名.常數名` 來訪問。
"""

# 模組級別常數
MEOWS_LIMIT = 3

for _ in range(MEOWS_LIMIT):
    print("meow")


# 類別常數與實例方法結合範例
class Cat:
    # 定義類常數（全大寫）
    MEOWS = 3

    def meow(self) -> None:
        """透過 Cat.MEOWS 訪問類常數來決定叫聲次數。"""
        for _ in range(Cat.MEOWS):
            print("meow")

if __name__ == "__main__":
    cat = Cat()
    cat.meow()



# =============================================================================
# 📚 CS50 Python - 類型提示 (Type Hints)、Mypy 檢查與 Docstrings 文件字串總結複習
# =============================================================================
"""
使用說明:
此檔案包含完整的程式碼以及詳細的觀念註解，專門用來解答「為什麼要這樣寫」的疑惑。
"""

# =============================================================================
# 觀念一: Python 的動態類型與類型提示 (Type Hints) 的價值
# =============================================================================
"""
【觀念解說】
- Python 預設是動態類型語言，不需要像 C/C++/Java 那樣強制宣告變數型態。
- 雖然靈活，但容易在執行時才發生型態錯誤（例如把字串傳給需要整數的函數）。
- Python 支援「類型提示（Type Hints）」，允許工程師在程式碼中標註變數與函數的預期型態（如 `n: int`）。
- ⚠️ 注意：Python 語言本身**不會**強制執行這些型態檢查，它只是一種提示與註解。
- 真正要發揮效用，需要依賴第三方靜態檢查工具（如 `mypy`）在執行前揪出潛在錯誤。
"""

# 初始版本：未加型態提示
def meow_v1(n):
    for _ in range(n):
        print("meow")

# 加上型態提示的版本
def meow_v2(n: int) -> None:
    """接收整數並印出指定次數的 meow（僅具備副作用）。"""
    for _ in range(n):
        print("meow")


# =============================================================================
# 觀念二: 使用 Mypy 靜態檢查工具在執行前發現錯誤
# =============================================================================
"""
【觀念解說】
- 安裝方式：在終端機輸入 `pip install mypy`。
- 使用方式：在終端機執行 `mypy 檔名.py`。
- 好處：
  1. 它不是給終端用戶看的工具，而是給「程序員」在發布或執行前檢查的防護網。
  2. 能在實際跑 `python` 崩潰之前，提早抓出類似「傳入字串卻預期整數」或「型態不相容」的錯誤。
"""


# =============================================================================
# 觀念三: 函數設計反思：副作用 (Side Effect) vs. 返回值 (Return Value)
# =============================================================================
"""
【觀念解說】
- 如果函數只有 `print()` 這種「副作用」，它其實不會回傳任何東西。
- 在 Python 中，沒有寫 `return` 的函數隱式回傳 `None`。
- 依循良好的單元測試與設計理念，讓函數**返回實際資料（如字串）**會比直接在內部 `print()` 更易於測試與重複利用。
- 同時搭配 `-> str` 等返回型態提示，能讓 `mypy` 幫我們檢查是否不小心把 `None` 當成字串來處理。
"""

def meow_v3(n: int) -> str:
    """接收整數 n，返回由換行符號隔開的 n 個 meow 字串。"""
    # 運用 Python 的字串乘法技巧，比寫迴圈更簡潔
    return "meow\n" * n


# =============================================================================
# 觀念四: Docstrings (文檔字符串) 與標準化寫法
# =============================================================================
"""
【觀念解說】
- PEP 257 標準化了 Python 的文檔撰寫方式：使用三引號(") 寫在函數內部最上方。
- Python 內建工具與外部文件生成器（如 Sphinx、pdoc）會自動掃描這些 Docstrings，
  替你把程式碼直接轉換成漂亮的網頁或 PDF 說明文件，省去手動寫文件的痛苦。
- 業界常見的規範之一是採用 `reStructuredText` 風格（如 `:param:`、`:type:`、`:raise:`、`:return:`），
  讓函數的輸入、型態、可能拋出的錯誤以及返回值一目了然。
"""

def meow_perfect(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    if not isinstance(n, int):
        raise TypeError("n 必須是整數")
    return "meow\n" * n


# =============================================================================
# 觀念五: 命令列參數 (sys.argv) 的基礎概念
# =============================================================================
"""
【觀念解說】
- 透過匯入 `sys` 模組，我們可以讀取從命令列（Terminal）傳入程式的參數 (`sys.argv`)。
- `sys.argv[0]` 通常是程式本身的檔名，後續的索引則對應使用者輸入的參數。
- 當專案變大、需要支援多種複雜的開關（如 `-n`、`-a`、`--number` 等位置錯綜複雜的參數）時，
  如果全部手動用 `if-else` 去判斷會變得極其繁雜。這時通常會需要依賴專門解析命令列參數的工具庫（例如 `argparse`）。
"""

import sys

def main_cli_demo() -> None:
    # 簡單示範命令列參數邏輯
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        try:
            n = int(sys.argv[2])
            for _ in range(n):
                print("meow")
        except ValueError:
            print("錯誤：-n 後方必須接一個整數")
    else:
        print("用法格式: python script.py 或 python script.py -n 次數")

if __name__ == "__main__":
    # 測試執行完美的 meow 函數
    result: str = meow_perfect(2)
    print(result, end="")



# =============================================================================
# 📚 CS50 Python - Argparse 參數解析器與星號解包運算子 (*args, **kwargs) 總結複習
# =============================================================================
"""
使用說明:
此檔案包含完整的程式碼以及詳細的觀念註解，專門用來解答「為什麼要這樣寫」的疑惑。
"""

# =============================================================================
# 觀念一: 使用 `argparse` 自動處理命令列參數 (CLI Arguments)
# =============================================================================
"""
【觀念解說】
- 如果需要讓使用者從終端機（Command Line）輸入較複雜的配置選項，手動用 `sys.argv` 搭配一堆 `if-else` 會變得很繁雜。
- `argparse` 是 Python 內建的強大命令列參數解析器，能自動幫我們處理解析、錯誤提示、型態轉換與產生說明書。
- `parser.parse_args()` 預設會自動讀取 `sys.argv`，並將結果封裝成一個物件（通常命名為 `args`）。
- 透過 `add_argument()` 可以定義參數、指定預設值 (`default`)、型態 (`type`) 以及說明文字 (`help`)。
- 只要輸入 `-h` 或 `--help`，程式就會自動印出標準的使用說明（Usage）。
"""

import argparse

# 建立參數解析器並加入描述
parser = argparse.ArgumentParser(description="Meow like a cat")
# 定義 -n 參數：預設值為 1，型態為整數，並附帶 help 說明
parser.add_argument("-n", default=1, help="number of times to meow", type=int)

# 解析參數（此處若在終端機輸入錯誤型態如 -n dog，argparse 會自動攔截並印出錯誤提示）
# args = parser.parse_args()


# =============================================================================
# 觀念二: 序列解包 (Unpacking with `*`)
# =============================================================================
"""
【觀念解說】
- 在呼叫函數時，如果參數放在列表（List）或元組（Tuple）中，不能直接傳入整個列表給多個獨立參數。
- 在變數前方加上一個星號 `*` 即可進行「序列解包」，它會將容器內的元素逐一拆開，作為獨立的位置參數傳入函數中。
- 注意：序列解包要求元素的數量必須與函數接收的位置參數數量相吻合，否則會引發 `TypeError`。
"""

def total_coins(galleons: int, sickles: int, knuts: int) -> int:
    return (galleons * 17 + sickles) * 29 + knuts

# 傳統列表寫法
coins_list = [100, 50, 25]
# 使用 * 進行列表解包，等同於 total_coins(100, 50, 25)
print(total_coins(*coins_list), "Knuts")


# =============================================================================
# 觀念三: 字典解包 (Dictionary Unpacking with `**`)
# =============================================================================
"""
【觀念解說】
- 字典（Dictionary）內部是由鍵值對（Key-Value）組成的。
- 在字典前方加上**兩個星號** `**`，可以進行「字典解包」。
- 它會把字典的鍵與值自動轉化為帶名稱的關鍵字參數（Keyword Arguments）傳入函數中（例如 `galleons=100, sickles=50...`）。
"""

coins_dict = {"galleons": 100, "sickles": 50, "knuts": 25}
# 使用 ** 進行字典解包
print(total_coins(**coins_dict), "Knuts")


# =============================================================================
# 觀念四: 可變數量參數 `*args` 與 `**kwargs`
# =============================================================================
"""
【觀念解說】
- 有時候我們不知道使用者會傳入多少個參數，這時可以在函數定義中使用 `*args` 和 `**kwargs`：
  1. `*args`（Arguments）：接收任意數量的「位置參數」，在函數內部被打包成一個**元組（Tuple）**。
  2. `**kwargs`（Keyword Arguments）：接收任意數量的「命名/關鍵字參數」，在函數內部被打包成一個**字典（Dictionary）**。
- 這是 Python 裡非常經典的慣例命名（名稱本身可自訂，但社群習慣用 `args` 與 `kwargs`）。
- 知名內建函數如 `print(*objects, sep=" ", end="\n")` 底層就是運用了這種可變參數的設計。
"""

def flexible_function(*args, **kwargs) -> None:
    print("收到的位置參數 (Tuple):", args)
    print("收到的命名參數 (Dict):", kwargs)

# 測試呼叫可變參數函數
if __name__ == "__main__":
    flexible_function(100, 50, 25, 5, mode="debug", verbose=True)



# =============================================================================
# 📚 CS50 Python - 函數式編程 (Functional Programming)、Map、Filter 與列表推導式 (List Comprehensions) 總結複習
# =============================================================================
"""
使用說明:
This file contains complete code and detailed conceptual annotations designed to answer "why it is written this way" for future review in VS Code.
"""

# =============================================================================
# 觀念一: 函數式編程 (Functional Programming) 與 Map 的應用
# =============================================================================
"""
【觀念解說】
- Python 除了命令式編程與物件導向（OOP）外，也支援「函數式編程（Functional Programming）」範式。
- 在函數式編程中，函數通常是獨立、無副作用的（不隨意修改外部全域狀態或單純 print），專注於「接收輸入並返回輸出」。
- `map(function, iterable, ...)` 是 Python 內建的函數式工具：
  1. 它會將指定的函數（例如 `str.upper`）「映射（套用）」到可迭代序列（如字串列表）的每一個元素上。
  2. 傳入函數時**不需要加括號**（傳遞函數本身而非調用結果），由 `map` 負責在內部替每個元素呼叫它。
"""

# 傳統使用可變參數接收單字並轉大寫的範例
def yell_traditional(*words: str) -> None:
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

# 使用 map 函數的函數式風格範例
def yell_with_map(*words: str) -> None:
    # 將 str.upper 映射到 words 序列的每個元素上
    uppercased_iter = map(str.upper, words)
    print(*uppercased_iter)


# =============================================================================
# 觀念二: 列表推導式 (List Comprehensions)
# =============================================================================
"""
【觀念解說】
- 雖然 `map` 很符合函數式編程，但在 Python 社群中，更常見且更「Pythonic」的做法是使用「列表推導式（List Comprehension）」。
- 語法結構：`[表達式 for 項目 in 可迭代物件]`。
- 它可以用極度簡潔的一行程式碼快速生成新列表，省去手動宣告空列表與寫 `for` 迴圈 `append` 的繁瑣步驟。
"""

def yell_with_list_comprehension(*words: str) -> None:
    # 透過列表推導式將每個單字轉大寫
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    yell_with_list_comprehension("This", "is", "CS50")


# =============================================================================
# 觀念三: 過濾資料：列表推導式的條件篩選 vs. Filter 函數
# =============================================================================
"""
【觀念解說】
- 除了轉換資料，我們經常需要從資料集中「過濾」符合條件的項目。
- 方法 A：在列表推導式後方加上 `if` 條件句（最常用、最直觀）。
- 方法 B：使用內建的 `filter(function, iterable)` 函數，它會要求傳入一個回傳布林值（True/False）的函數，來決定是否保留該元素。
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# 方式 A：使用帶條件的列表推導式（過濾出葛來分多學生並提取名字）
gryffindors_lc = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]


# =============================================================================
# 觀念四: 結合 Filter 函數與 Lambda 匿名函數
# =============================================================================
"""
【觀念解說】
- `filter(function, iterable)` 的第一個參數必須是一個會回傳 `True` 或 `False` 的函數。
- 如果某個判斷邏輯只會用這麼一次，專門定義一個具名函數會顯得冗長。此時可以使用 `lambda` 創建「匿名函數」。
- 語法：`lambda 參數: 運算式`（會自動回傳運算結果）。
"""

# 使用 filter 搭配 lambda 表達式過濾出葛來分多學院的字典物件
gryffindors_filtered = filter(lambda s: s["house"] == "Gryffindor", students)

if __name__ == "__main__":
    # 將過濾出來的學生物件透過 sorted 與 lambda 依照名字進行排序後印出
    for gryffindor in sorted(gryffindors_filtered, key=lambda s: s["name"]):
        print(gryffindor["name"])



# =============================================================================
# 📚 CS50 Python - 字典推導式 (Dictionary Comprehensions)、Enumerate 與生成器 (Generators / Yield) 總結複習
# =============================================================================
"""
使用說明:
This file contains complete code and detailed conceptual annotations designed to answer "why it is written this way" for future review in VS Code.
"""

# =============================================================================
# 觀念一: 字典推導式 (Dictionary Comprehensions)
# =============================================================================
"""
【觀念解說】
- 類似於列表推導式（List Comprehensions），Python 也支援「字典推導式」。
- 語法特徵：外層使用花括號 `{}`，內部透過 `鍵: 值 for 項目 in 可迭代物件` 的格式來快速生成字典。
- 這能省去傳統用 `for` 迴圈逐一初始化或新增索引鍵值的繁瑣步驟，讓程式碼更簡潔。
"""

students = ["Hermione", "Harry", "Ron"]

# 傳統建立字典列表的方法
gryffindors_list = []
for student in students:
    gryffindors_list.append({"name": student, "house": "Gryffindor"})

# 使用字典推導式直接建立以學生名字為鍵、學院為值的字典
gryffindors_dict = {student: "Gryffindor" for student in students}


# =============================================================================
# 觀念二: 使用 `enumerate()` 同時獲取索引與值
# =============================================================================
"""
【觀念解說】
- 當我們在迴圈中既需要元素的值，又需要它的索引（Index，例如排名或行號）時，傳統做法需要搭配 `range(len(...))`。
- Python 內建的 `enumerate(iterable, start=0)` 能夠在迭代序列時，同時返回「索引」與「對應的值」。
- 這樣就不需要透過繁瑣的數字索引去存取列表，程式碼更直覺、更符合 Pythonic 風格。
"""

def print_student_rankings() -> None:
    students_list = ["Hermione", "Harry", "Ron"]
    # 透過 enumerate 同時取得索引 i 與元素 student（可設定 start=1 從 1 開始編號）
    for i, student in enumerate(students_list, start=1):
        print(i, student)


# =============================================================================
# 觀念三: 記憶體危機與生成器 (Generators) 與 `yield` 關鍵字
# =============================================================================
"""
【觀念解說】
- 當函數需要生成或處理海量數據（例如一百萬筆資料）時，如果把所有資料一次性塞進列表並用 `return` 返回，
  會導致記憶體（RAM）耗盡甚至讓程式崩潰。
- **生成器 (Generator)** 的核心概念是「按需生成、用完即丟」，每次只返回一個元素。
- 把函數中的 `return` 改為 `yield`，就能讓該函數變成一個生成器：
  1. 程式執行到 `yield` 時會暫停（Pause），並將當前的值回傳給呼叫方。
  2. Python 會自動記住函數目前的執行狀態（State）。
  3. 當下一次迴圈再度向它索取資料時，它會從上次暫停的地方繼續往下執行。
- `yield` 回傳的是一個**迭代器 (Iterator)**，它消耗極少的記憶體，非常適合處理大數據。
"""

def sheep_generator(n: int):
    """使用 yield 逐一生成指定數量的羊字串，避免一次性佔滿記憶體。"""
    for i in range(n):
        yield "🐑" * i


# =============================================================================
# 觀念四: 額外套件應用簡介 (如 pyttsx3)
# =============================================================================
"""
【觀念解說】
- Python 生態系擁有極為豐富的第三方庫。
- 例如 `pyttsx3` 是一個文字轉語音（Text-to-Speech）的離線庫，可以透過初始化引擎並調用 `say()` 與 `runAndWait()` 來讓電腦朗讀字串。
"""

import pyttsx3

def text_to_speech_demo() -> None:
    # 初始化語音引擎（實際執行需確保已安裝 pip install pyttsx3 與相關依賴）
    # engine = pyttsx3.init()
    # engine.say("Hello CS50")
    # engine.runAndWait()
    pass


if __name__ == "__main__":
    print("--- 執行字典推導式結果 ---")
    print(gryffindors_dict)
    
    print("\n--- 執行 Enumerate 排名範例 ---")
    print_student_rankings()
    
    print("\n--- 執行生成器 (Yield) 範例 (產出 3 隻羊) ---")
    for s in sheep_generator(3):
        print(s)