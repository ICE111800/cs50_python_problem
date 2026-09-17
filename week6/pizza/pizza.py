import csv
import sys
from tabulate import tabulate

def main():
    file_name = determine_command_line_arguments()
    table = read_csv(file_name)
    # 使用 tabulate 印出表格，headers="keys" 會自動抓取字典的 Key 作為標題

    print(tabulate(table, headers="keys", tablefmt="grid"))

def determine_command_line_arguments() -> str:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len (sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return file_name


def read_csv(file_name: str) -> list:
    table = []
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # DictReader 會自動把第一行當成 Key (例如 'Sicilian Pizza', 'Small', 'Large')
                # 我們直接把整行 row（它本質上就是個有序字典）塞進清單裡即可
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return table

if __name__ == "__main__":
    main()



"""
============================================================
【Python 複習筆記】Pizza Py 與字串引號的終極判斷心法
============================================================

1. 模組化資料讀取：csv.reader vs csv.DictReader
   - csv.reader (清單包清單 List of Lists):
     * 每一行讀進來都是純粹的字串陣列 (List)。
     * 表頭與資料平起平坐，通常需要手動分離 (例如用 table[0] 當表頭，table[1:] 當資料)。
   - csv.DictReader (字典清單 List of Dictionaries):
     * 自動把第一行抓下來當作每一行字典的「Keys（欄位名稱）」。
     * 搭配 tabulate 時，設定 headers="keys" 可以讓 tabulate 自動抓取字典的 Key 當作表頭。

2. 終極引號迷思：到底什麼時候該加 ""？
   - 黃金判斷原則：
     * **有加引號 ""** = **資料本身 / 固定的文字內容 / 函式專用的文字指令選項**。
       (例：`"csv"`, `"grid"`, `"keys"`, `user["name"]` 中固定的 Key 名稱)
     * **沒有引號** = **變數、函式名稱、程式碼語法、參數名稱**。
       (例：`file_name`, `tabulate(..., headers=...)`, `import csv`)

   - 經典對比案例：
     * `user["name"]`：有引號 $\rightarrow$ 代表直接指定要找叫 `"name"` 的那個固定的欄位標籤。
     * `user[key]`：沒有引號 $\rightarrow$ 代表 `key` 是一個變數，去查這個變數裡面裝的是什麼字串。
     * `tabulate(table, headers="keys", tablefmt="grid")`：
       - `headers`（沒引號）是 tabulate 規定的參數名稱。
       - `"keys"`（有引號）是傳給 headers 的固定文字指令。
       - `"grid"`（有引號）是傳給 tablefmt 的排版樣式指令。

3. 防禦性編程與命令列檢查
   - 務必維持「命令列防禦三本柱」：
     1. 檢查引數數量是否剛好 (Too few / Too many)。
     2. 檢查檔案副檔名是否合法 (`.endswith(".csv")`)。
     3. 確保開檔時使用 try...except 攔截 `FileNotFoundError`。
============================================================
"""
