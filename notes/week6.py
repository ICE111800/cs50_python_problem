"""
=============================================================================
📚 CS50 Python - 檔案輸入輸出 (File I/O) 與進階排序觀念總結複習
=============================================================================
使用說明:
此檔案包含完整的程式碼以及詳細的觀念註解，專門用來解答「為什麼要這樣寫」的疑惑。
"""

# =============================================================================
# 觀念一:為什麼需要檔案 (File I/O)？記憶體與硬儲存體的差別
# =============================================================================
"""
【觀念解說】
- 如果只用 Python 的 list（列表）來存資料，資料是暫時存在電腦的「記憶體（RAM）」中。
- 一旦程式結束（退出終端機），記憶體被清空，資料就會全部消失。
- 為了讓資料可以「持久化保存」（關掉程式後下次打開還在），我們必須把資料寫入檔案（存到硬碟或雲端）。
"""

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")


# =============================================================================
# 觀念二:寫入檔案的兩種模式:w (Write) vs a (Append)
# =============================================================================
"""
【觀念解說 - 為什麼用 "w" 會把舊資料洗掉？】
- open("names.txt", "w") 的 "w" 代表 write（寫入）。
- 如果檔案不存在，它會自動幫你建立；但如果檔案**已經存在**，它會無條件清空裡面的所有舊內容，從頭寫入。
- 所以如果想累積多筆資料，不能用 "w"，必須用 "a"（append，附加在檔案最後面）。
"""

# 示範 w 模式（會覆蓋舊檔案）
name = input("What's your name? ")
file = open("names.txt", "w")
file.write(name)
file.close()  # 為什麼一定要 close？因為要告訴作業系統把資料真正寫入硬碟並釋放資源


# 示範 a 模式（保留舊資料，串接在後方）
name = input("What's your name? ")
file = open("names.txt", "a")
# 為什麼要手動加 "\n"？
# 因為 write() 函數很原始，你給它什麼字串它就印什麼，不會像 print() 一樣自動幫你換行。
file.write(f"{name}\n")
file.close()


# =============================================================================
# 觀念三:為什麼要用 with 上下文管理器？
# =============================================================================
"""
【觀念解說】
- 在寫程式時，常常會忘記寫 file.close()，這可能會導致檔案損壞或資源佔用。
- 透過 `with open(...) as file:`，Python 會建立一個安全的「上下文」。
- 當程式離開這個縮排區塊時，Python **會自動在背景幫你調用 close()**，既安全又簡潔。
"""

name = input("What's your name? ")

with open("names.txt", "a") as file: 
    file.write(f"{name}\n")


# =============================================================================
# 觀念四:為什麼讀取檔案時需要 rstrip()？
# =============================================================================
"""
【觀念解說】
- 我們在寫入時加了 `\n`（換行符），所以當 Python 用迴圈逐行讀取檔案時，每一行的結尾其實都帶有一個看不見的換行符。
- 如果直接用 `print("hello,", line)`，print 本身又會自動換行，就會導致畫面出現難看的「雙重空行」。
- 使用 `line.rstrip()` 可以把字串右側所有多餘的空白和換行符切掉，把主導權交還給 print 函數。
"""

with open("names.txt") as file:  # 預設模式就是 "r" (read，讀取)
    for line in file:
        print("hello,", line.rstrip())


# =============================================================================
# 觀念五:為什麼要用 CSV 格式與 split() 進行字串解包？
# =============================================================================
"""
【觀念解說】
- 如果我們想在一個檔案裡存不只「名字」，還想存「學院」（例如:Hermione,Gryffindor），混在一起存會很亂。
- 業界標準會使用 CSV（Comma-Separated Values，逗號分隔值）。
- `line.rstrip().split(",")` 的作用:
  1. 先用 rstrip() 去除結尾換行。
  2. 用 split(",") 以逗號為切割點，把一行字串拆成一個列表（例如:["Hermione", "Gryffindor"]）。
  3. 透過 Python 的「解包（Unpacking）」特性，直接把列表左邊的值給 `name`，右邊給 `house`。
"""

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


# =============================================================================
# 觀念六:為什麼要使用字典（Dictionaries）來取代純字串？
# =============================================================================
"""
【觀念解說】
- 如果我們把整句話組合成字串（例如 "Hermione is in Gryffindor"）才拿去排序，
  排序時其實是去比對英文字母開頭，這樣很不嚴謹。
- 更好的做法是把資料結構化:用「字典（Dictionary）」把 `name` 和 `house` 獨立分開儲存，
  再把多個字典放進一個 `students` 列表裡，這樣我們就能精準知道誰是誰。
"""

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # 建立一個字典，明確對應 key 與 value
        student = {"name": name, "house": house}
        students.append(student)


# =============================================================================
# 觀念七:為什麼 sorted() 需要搭配 key 參數與自訂函數？（核心難點）
# =============================================================================
"""
【觀念解說 - 為什麼 sorted() 需要我們提供函數？】
1. 當你對一個「包含字典的列表」執行 sorted(students) 時，Python 其實很困惑:
   「這是一個字典，我要拿『name』來排，還是拿『house』來排？我不知道怎麼比較它們的大小！」
2. Python 的開發者在設計 `sorted()` 時，不可能預先知道你以後會寫出什麼樣的字典結構，
   所以他們設計了 `key` 這個命名參數。
3. `key` 的意思是:「我（sorted）負責幫你排序，但『要拿什麼欄位來比大小』這件事交給你決定。
   請你寫一個函數交給我，我每看一個學生，就會自動執行一次你給我的函數，用它回傳的值來排隊。」

【為什麼 get_name 後面不能加括號 ()？】
- 如果寫 `key=get_name()`，代表你現在就要立刻執行這個函數。
- 寫 `key=get_name`（不加括號），代表「把這個函數本身（作為一個物件）交給 sorted」，
  讓 sorted 在底下的排序過程中，需要時才去呼叫它。這就是「把函數當作參數傳遞」的精髓！
"""



"""
=============================================================================
📚 CS50 Python - 進階排序、CSV 檔案處理與 PIL 圖像套件複習筆記
=============================================================================
使用說明:
此檔案包含完整的程式碼以及詳細的觀念註解，專門用來解答「為什麼要這樣寫」的疑惑。
"""

# =============================================================================
# 觀念一:為什麼 sorted() 需要搭配 key 與自訂函數？
# =============================================================================
"""
【觀念解說】
- 當我們把 CSV 讀進來並存成「字典列表」（例如:`{"name": "Harry", "house": "Gryffindor"}`）時，
  如果直接執行 `sorted(students)`，Python 會不知道要拿哪一個欄位來比大小。
- Python 的開發者在設計 `sorted()` 時，預留了一個 `key` 參數。
- 它的意思是:「我（sorted）負責幫你排序，但你要拿什麼欄位來比，請交給我一個函數，
  我會在排序時自動把每個字典丟進你的函數裡，用它回傳的值來排隊！」
"""

students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

# 定義一個專門提取姓名的函數
def get_name(student):
    return student["name"]

# 帶入 key=get_name（注意:函數後面絕對不能加括號 ()，我們是把函數本身當作物件傳過去）
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


# 如果想按學院（house）進行反向排序（reverse=True），可以這樣寫:
def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")


# =============================================================================
# 觀念二:為什麼要使用 Lambda（匿名函數）？
# =============================================================================
"""
【觀念解說】
- 像 `get_name` 或 `get_house` 這種簡單的函數，通常「只會在 sorted 裡面用這麼一次」。
- 為了特地定義它而寫 `def get_name(...)` 會顯得程式碼很冗長。
- Python 提供了 **`lambda`（匿名函數）**:沒有名字、不用 def、不用寫 return。
- 語法:`key=lambda 參數: 回傳的值`
"""

# 使用 lambda 改寫，效果完全一樣，但更簡潔:
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


# =============================================================================
# 觀念三:為什麼手動用 split(",") 處理 CSV 會遇到大麻煩？
# =============================================================================
"""
【觀念解說】
- 假設 CSV 的資料變成了這樣（地址裡面包含逗號）:
  Harry,Number Four, Privet Drive
- 如果我們用原本的 `line.split(",")` 去切，Python 會把這一行切成 3 個部分（名字、地址前半、地址後半），
  導致我們預期用 `name, home = ...` 進行「解包」時直接發生 **ValueError（值太多無法解包）**。
- 如果為了避開這個問題去手動寫「只分割不在引號內的逗號」的程式碼，會變得極其複雜。
- 幸好，Python 內建了專門處理 CSV 的官方庫:`import csv`！
"""


# =============================================================================
# 觀念四:使用內建的 csv 模組與 reader
# =============================================================================
"""
【觀念解說】
- `csv.reader(file)` 會自動幫我們處理引號、逗號等邊界情況，不用擔心地址裡的逗號把程式搞崩。
- 它讀出來每一行會是一個「列表（row）」:`row[0]` 是第一欄，`row[1]` 是第二欄。
"""

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        # 可以用列表索引存取，也可以直接在 for 迴圈中解包
        students.append({"name": row[0], "home": row[1]})


# =============================================================================
# 觀念五:使用 csv.DictReader（防禦性編程的最佳實踐）
# =============================================================================
"""
【觀念解說】
- 如果使用 `row[0]` 和 `row[1]`，萬一有一天別人打開 CSV 檔案，把「名字」跟「家鄉」的欄位順序對調了，
  程式就會抓錯資料。
- 透過 **`csv.DictReader(file)`**，它會自動把 CSV 的「第一行（表頭）」當作字典的 Key（鍵）。
- 這樣我們就可以直接寫 `row["name"]` 和 `row["home"]`。
- 好處:就算別人把欄位左右調換，或者未來在中間插入了新的欄位（例如 house），只要表頭名字對了，
  我們的 Python 程式就**完全不用修改**也不會崩潰！這就是「防禦性編程」。
"""

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # 透過欄位名稱（Key）來取值，不再依賴固定索引位置
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# =============================================================================
# 觀念六:寫入 CSV 檔案:csv.writer vs csv.DictWriter
# =============================================================================
"""
【觀念解說】
- 寫入資料時若用 `"a"`（附加模式），可以不斷在檔案後方新增資料。
- `csv.writer` 需要你傳入一個串列（List），例如 `[name, home]`。
- `csv.DictWriter` 則允許你傳入一個字典，但必須預先指定 `fieldnames`（欄位順序），
  這樣它才知道要把字典裡的資料對應寫入哪一個欄位，同時它也會自動幫含有逗號的字串加上引號轉義。
"""

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# 使用 DictWriter 寫入範例:
with open("students.csv", "a") as file:
    # 必須指定 fieldnames 定義欄位順序
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # 傳入字典進行寫入，鍵值對的順序不影響結果
    writer.writerow({"name": name, "home": home})


# =============================================================================
# 觀念七:使用外部套件 Pillow 處理圖像並製作 GIF 動畫
# =============================================================================
"""
【觀念解說】
- Python 的強大之處在於有非常多現成的強大第三方庫（例如處理圖像的 `PIL` / `Pillow`）。
- 我們可以透過終端機傳入多個命令列參數（利用 `sys.argv[1:]` 略過程式檔名本身），
  讀取多張靜態圖片，並將它們組合成一個會動的 GIF 動畫。
"""

import sys
from PIL import Image

images = []

# sys.argv[1:] 代表從命令列參數的第二個開始抓（排除掉檔名 costumes.py）
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# 將第一張圖片作為基礎，把其餘圖片串接進去並存檔為 GIF
images[0].save(
    "costumes.gif", 
    save_all=True,               # 代表要保存所有的影格（動態圖）
    append_images=[images[1]],   # 帶入後續要串接的圖片列表
    duration=200,                # 每張圖片持續的時間（毫秒）
    loop=0                       # 0 代表無限循環播放
)


"""
=============================================================================
📚 專題對比複習:csv.reader vs csv.DictReader 以及 csv.writer vs csv.DictWriter
=============================================================================
"""

# =============================================================================
# 🔍 讀取對比:csv.reader 與 csv.DictReader 的差異在哪裡？
# =============================================================================
"""
【核心差異總結】
1. csv.reader:
   - 讀出來的每一行(row)是一個「**列表 (List)**」。
   - 你必須用**索引數字**來抓資料（例如:row[0] 是名字、row[1] 是家鄉）。
   - 缺點:如果 CSV 檔案的欄位順序被別人對調，你的程式就會抓錯資料甚至報錯。

2. csv.DictReader:
   - 讀出來的每一行是一個「**字典 (Dictionary)**」。
   - 它會自動把 CSV 的第一行（表頭）當作 Key，讓你用**欄位名稱**來抓資料（例如:row["name"]）。
   - 優點:具備「防禦性編程」能力。就算別人把欄位順序對調、或亂加新欄位，只要表頭名字對，程式就完全不會壞！
"""

# --- 【寫法 A】使用 csv.reader（依賴固定位置索引） ---
import csv

students_reader_list = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        # ⚠️ 必須用 row[0] 和 row[1] 這種固定數字索引
        # 如果 CSV 裡面變成 [home, name]，這裡的資料就會全部對錯！
        students_reader_list.append({"name": row[0], "home": row[1]})


# --- 【寫法 B】使用 csv.DictReader（依賴表頭名稱、推薦！） ---
students_dict_reader_list = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # ✅ 直接用欄位名字 row["name"] 與 row["home"]
        # 就算 CSV 欄位左右對調，Python 也能精準對應，安全又聰明！
        students_dict_reader_list.append({"name": row["name"], "home": row["home"]})


# =============================================================================
# ✍️ 寫入對比:csv.writer 與 csv.DictWriter 的差異在哪裡？
# =============================================================================
"""
【核心差異總結】
1. csv.writer:
   - 寫入時，你需要傳入一個「**列表 (List)**」（例如:[name, home]）。
   - 你必須自己確保列表中元素的「順序」跟檔案欄位完全一致，否則資料會寫錯行。

2. csv.DictWriter:
   - 寫入時，你可以直接傳入一個「**字典 (Dictionary)**」（例如:{"name": name, "home": home}）。
   - 需要在最前面宣告 `fieldnames=["name", "home"]` 來綁定欄位順序。
   - 優點:傳入的字典裡鍵值對順序可以隨意調換，程式依然會乖乖依照 fieldnames 指定的順序寫入檔案，非常直覺安全！
"""

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# --- 【寫法 A】使用 csv.writer（傳入列表） ---
# 需手動確保順序為 [name, home]
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


# --- 【寫法 B】使用 csv.DictWriter（傳入字典，推薦！） ---
# 需先宣告 fieldnames 規定欄位順序，寫入時直接帶入字典
with open("students.csv", "a", newline="") as file:
    # 1. 告訴寫入器有哪些欄位與其順序
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    
    # 2. 傳入字典（就算寫成 {"home": home, "name": name} 順序顛倒也沒關係，它會自動對號入座）
    writer.writerow({"name": name, "home": home})