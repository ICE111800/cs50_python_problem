import sys

def main() -> None:
    file_name = determine_command_line_arguments()
    row_count = count_rows(file_name)
    print(row_count)
    
def determine_command_line_arguments() -> str:
    """防禦性檢查命令列引數：確保數量剛好為 2 且副檔名為 .py"""
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    # 確保副檔名為 .py（防禦性檢查大小寫或結尾）
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")

    return file_name

def count_rows(file_name: str) -> int:
    """讀取指定的 Python 檔案，計算排除空白行與註解後的程式碼行數"""
    total_count = 0
    try:
        with open(file_name) as file:
            for line in file:
                stripped_line = line.lstrip()
                # 如果是空白行或是以 # 開頭的註解行，直接跳過
                if stripped_line == "" or stripped_line.startswith("#"):
                    continue
                total_count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return total_count


if __name__ == "__main__":
    main()



"""
============================================================
【Python 複習筆記】命令列引數檢查、副檔名驗證與架構分工
============================================================

1. 命令列引數的防禦性檢查 (Command-Line Arguments)
   - 透過 `sys.argv` 接收終端機輸入。
   - 務必在主邏輯執行前做好「防禦性三本柱」：
     * 檢查引數數量是否剛好（Too few / Too many）。
     * 檢查檔案副檔名是否合法。
     * 檢查檔案是否存在（使用 try...except 攔截 FileNotFoundError）。

2. 為什麼推薦用 .endswith() 取代切片 ([-3:])？
   - 切片 [-3:] 的盲點：
     * 依賴固定的字串長度（假設副檔名剛好是 3 個字）。
     * 當遇到不同長度的副檔名（例如 .pyw 有 4 個字）時，邏輯會直接失效，必須重寫。
   - .endswith() 的優勢 (Pythonic)：
     * 語意明確：一眼就能看出意圖是「檢查結尾」。
     * 支援多重比對：可直接傳入 Tuple 同時檢查多種副檔名，例如：
       `if file_name.endswith((".py", ".pyw")):`

3. 變數與字串常數的區別 (Variables vs String Literals)
   - 錯誤示範：`with open("file_name")` -> 帶引號代表尋找一個檔名剛好叫 "file_name" 的檔案。
   - 正確示範：`with open(file_name)` -> 不帶引號，代表去讀取 `file_name` 變數裡裝的實際檔名（如 "hello.py"）。

4. 模組化架構設計：main() 與自訂函式的分工
   - main() 函式（指揮官 / 導演）：
     * 負責主導流程（Orchestration）。
     * 決定步驟的執行順序（先檢查參數 -> 再讀檔算行數 -> 印出結果）。
   - 自訂函式（專業工匠 / 工具箱）：
     * 具備「高內聚力」，專心做好單一工具該做的事（如 `determine_command_line_arguments`、`count_rows`）。
     * 達到「用了一次還能再用」的重用性。
============================================================
"""
