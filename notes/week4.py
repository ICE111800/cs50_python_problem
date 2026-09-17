"""
=============================================================================
📚 Python 核心模組、命令行與效率工具總複習筆記 (CS50 觀念整理)
=============================================================================
使用說明：
此檔案整合了你目前的課堂筆記、程式碼範例、觀念補充以及鍵盤快捷鍵。
你可以直接在 VS Code 中閱讀註解與程式碼，或執行特定的程式碼段落來複習！
"""

# =============================================================================
# 一、 模組與套件 (Modules & Packages)
# =============================================================================

"""
1. 什麼是模組 (Modules)？
   - 本質上就是函式庫 (Library)，包含內置函數或其他功能特性。
   - 核心優勢：將重複複用的程式碼抽離，避免冗餘副本，站在巨人的肩膀上開發。

2. 載入方式的差別：
   - 全面導入 (`import`)：須通過模組名稱調用，維持獨立作用域，避免命名衝突。
   - 精準導入 (`from ... import ...`)：直接將特定函數加載到當前命名空間，代碼簡潔。
"""

# 【範例 1】全面導入 import random
import random

coin = random.choice(["heads", "tails"])
print("Random Coin:", coin)

# 【範例 2】精準導入 from random import choice
from random import choice

coin_2 = choice(["heads", "tails"])
print("Random Choice:", coin_2)

# 【範例 3】random.randint(a, b) 隨機範圍內整數
number = random.randint(1, 10)
print("Random Number (1-10):", number)

# 【範例 4】random.shuffle(x) 打亂順序 (會直接修改傳入的列表本身，不返回新列表)
cards = ["jack", "queen", "king"]
random.shuffle(cards)
print("Shuffled Cards:")
for card in cards:
    print(" -", card)

# 【範例 5】statistics 統計相關模組
import statistics

avg_score = statistics.mean([100, 90])
print("Statistics Mean:", avg_score)

# command-line arguments 命令行參數
# 允許你不必像調用 python 的 input函數那樣在程序運行中等待用戶輸入
# 允許你在執行命令行時，直接向程序提供輸入參數
# python hello.py ...

# sys (system)
# sys.argv (argument vector) 
# 參數向量，指的是用戶在按下enter之前在命令行中輸入的所有單詞的列表
# 所有這些內容都會變成通過python以sys.argv變數的形式提供給你
import sys

print("hello, my name is", sys.argv[1])



# =============================================================================
# 二、 CS50 Python - 命令行參數 (Command-Line Arguments) 與錯誤處理演進
# =============================================================================

import sys

# 1. 基本概念與 IndexError
# -----------------------------------------------------------------------------
# 執行範例：python week4.py ice
# sys.argv 是一個列表：
# - index[0] 存放的是程式本身的名字 (week4.py)
# - index[1] 才是存放我們傳入的名字參數 (ice)
# 如果用戶甚麼都不輸入（只打 python week4.py），訪問 sys.argv[1] 會引發錯誤：
# IndexError: list index out of range


# 2. 解決一：使用 try...except 捕捉 IndexError
# -----------------------------------------------------------------------------
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


# 3. 解決二：使用條件判斷式 (if...elif...else)
# -----------------------------------------------------------------------------
# 檢查參數數量，限制只能剛好傳入一個參數
# 輸入 python week4.py           -> 太少 (Too few arguments)
# 輸入 python week4.py David Malon -> 太多 (Too many arguments)
# 輸入 python week4.py David     -> 剛好一個參數，正常執行
# 💡 註：如果要傳全名，可以用雙引號包起來當作一個參數：python week4.py "David Malan"

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])


# 4. 解決三：從設計角度優化（但隱藏潛在 Bug）
# -----------------------------------------------------------------------------
# 老師提到：如果能不用把真正關心的 code 藏進 else 語句裡會更好。
# 但如果寫成下面這樣，會引發新的 Bug：
# 如果輸入 python week4.py，雖然會印出 "Too few arguments"，
# 但緊接著還是會執行 print，因為盲目訪問了 sys.argv[1]，導致 IndexError 再次發生！

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
#
# print("hello, my name is", sys.argv[1])  <-- 這裡會出事


# 5. 解決四：使用 sys.exit() 在系統幫助下完美退出程式
# -----------------------------------------------------------------------------
# 利用 sys.exit() 直接終止程式。
# 現在可以確信：只要執行到最後一行，前面的錯誤情況都已經被攔截檢查過了，
# 因此可以安全地假設 sys.argv[1] 確實有元素，不會再出現 IndexError。

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


# 6. 命令行傳入多個參數與切片 (Slices)
# -----------------------------------------------------------------------------
# 如果不再限制命令行中的單詞數量，想接收多個名字：
# 執行範例：python week4.py David Carter Rongxin

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# 【問題】如果直接用 for 迴圈遍歷 sys.argv：
# for arg in sys.argv:
#     print("hello, my name is", arg)
# 會發現連程式名稱本身 (week4.py) 都一起被印出來了！

# 【解決辦法：列表切片 Slices】
# 切片一個列表可以獲取它的子集（[起始位置 : 結束位置]）。
# 使用 sys.argv[1:] 略過第一個元素（程式檔名），只保留後面的參數：
for arg in sys.argv[1:]: 
    print("hello, my name is", arg)

# 【其餘範例：前後切片】
# 使用負數索引從最後面開始切，可以同時切掉第一個（檔名）和最後一個元素：
# for arg in sys.argv[1:-1]:
#     print("hello, my name is", arg)



# =============================================================================
# 三、 第三方套件與 Pip (Packages & PyPI)
# =============================================================================

"""
1. 套件 (Packages)：超越 Python 自帶庫的第三方擴展。
2. PyPI (Python Package Index)：官方第三方套件倉庫 (pypi.org)。
3. Pip：Python 的包管理器。
   - 安裝指令範例：pip install cowsay
"""

# 【範例 7】使用 cowsay 第三方套件
# 需先在終端機執行: pip install cowsay
"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
"""


# =============================================================================
# 四、 開發效率：鍵盤快捷鍵總整理 (Windows 系統)
# =============================================================================

"""
【一、 游標移動的高速公路（配合 Ctrl）】
- Ctrl + ← / →          ：以「單字」為單位左右跳躍，快速跨越變數名稱。
- Ctrl + Home / End      ：直接跳到整個檔案的最開頭或最結尾。

【二、 精準選取文字（配合 Shift）】
- Shift + Home / End     ：一邊移動游標，一邊將整行文字反白選取。
- Ctrl + Shift + ← / →   ：以單字為單位精準反白選取文字。

【三、 VS Code 編輯與修改神器】
- Ctrl + D               ：選取目前游標所在的單字（多按幾次可啟動多重游標一起改）。
- Alt + ↑ / ↓            ：將目前整行程式碼往上或往下移動。
- Ctrl + Shift + K       ：直接刪除整行。
- Ctrl + /               ：快速註解 / 取消註解（自動加或移除 #）。
"""



# =============================================================================
# CS50 Python - APIs、JSON 資料處理與自定義模組 (Custom Modules)
# =============================================================================

import json
import sys
import requests

# =============================================================================
# 五、 APIs 與 requests 庫（以 iTunes API 為例）
# =============================================================================

"""
1. 什麼是 API (Application Programming Interface)？
   - 應用程式編程介面，更多指的是第三方服務，透過編寫程式碼與之互動。
   - 許多（並非全部）API 都部署在網際網路上，可透過 URL 請求獲取資源。

2. requests 庫
   - 透過 Python 程式碼發送網路請求，就像自己使用瀏覽器一樣。
   - 可自動獲取 http 或 https 開頭的 URL 資源。
   - 安裝指令：pip install requests

3. 閱讀 API 文檔與參數：
   - Apple 提供了 iTunes API 用來搜索音樂。
   - 網址範例：https://itunes.apple.com/search?entity=song&limit=1&term=weezer
     * entity=song：指定搜索類型為歌曲（而非專輯或歌手）。
     * limit=1：限制只返回一筆結果。
     * term=weezer：指定搜索的歌手或樂團名稱。

4. JSON (JavaScript Object Notation)
   - 瀏覽器直接打開 API 連結會看到一堆難懂的標準文字格式 (JSON)。
   - 「語言無關」：不必使用 JavaScript，Python 或其他語言也能輕鬆讀取或編寫 JSON。
"""

# 【範例 1】基本的 requests 請求與回應
# 執行指令範例：python week4_api.py weezer
if len(sys.argv) != 2:
    sys.exit("Too few arguments")

# 發送 GET 請求給 iTunes API
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
# Apple 伺服器返回本質是 JSON，但 requests 庫會自動把它轉換成 Python 字典格式
# print(response.json())


# 【範例 2】使用 json.dumps 美化輸出格式
# response.json() 的結構類似：{'resultCount': 1, 'results': [...]}
# 透過 json.dumps 的 indent=2 可以讓列印出來的 JSON 內容縮排 2 個空格，變得漂亮易讀
print(json.dumps(response.json(), indent=2))


# 【範例 3】抓取多筆數據並解析列表
# 假設我們將 limit 設為 50，並撈出裡面每一首歌的曲名 (trackName)
response_multi = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]
)
o = response_multi.json()
print("\n--- 搜尋到的歌曲列表 ---")
for result in o["results"]:
    print(result["trackName"])


# =============================================================================
# 六、 自定義模組 (Custom Modules) 與 sayings.py 範例
# =============================================================================

"""
【錯誤示範：在 sayings.py 底部直接調用 main()】
如果我們在 sayings.py 的最底部直接寫了 main()：
    def main():
        hello("world")
        goodbye("world")
    ...
    main()  <-- 直接無條件調用

當你在另一個檔案 (say.py) 中寫入 `from sayings import hello` 時：
Python 會從頭到尾、從左到右讀取 sayings.py，
這意味著只要 Python 加載這個檔案，底部的 main() 就會被無條件執行！
這會導致你在執行 `python say.py David` 時，意外印出不需要的 world 招呼語。
"""

# =============================================================================
# 七、 正確做法：使用 __name__ == "__main__"
# =============================================================================

"""
【__name__ 變數的機制】
- 當你直接從命令列運行一個檔案時（例如：python sayings.py），
  Python 會自動將該檔案的 __name__ 變數設為 "__main__"。
- 當這個檔案是被別人當作模組導入時（例如：from sayings import hello），
  __name__ 的值就不會是 "__main__"，而是該模組的檔案名稱（"sayings"）。

透過這個特性，我們可以把 main() 的調用包裹在條件語句中，
讓它「只有在直接執行該檔案時才跑，被導入時則被忽略」。
"""


# 模擬 sayings.py 模組的正確寫法結構：
def sayings_main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


# 關鍵保護機制：
# 如果是直接執行此檔案，才會執行 main；如果是被 import 則會被安全忽略
if __name__ == "__main__":
    sayings_main()