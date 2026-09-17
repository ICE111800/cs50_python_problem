import requests
import sys

def main():
    # ---------------------------------------------------------
    # 參數數量檢查 (使用 if - LBYL 原則：先看再走)
    # ---------------------------------------------------------
    # sys.argv 是一個 list，包含了執行程式時的命令列參數。
    # sys.argv[0] 永遠是程式名稱 (例如 'bitcoin.py')。
    # 所以如果你要使用者傳入 1 個參數，總長度必須要是 2。
    if len(sys.argv) < 2:
        sys.exit("\nMissing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # ---------------------------------------------------------
    # 型態轉換與錯誤捕捉 (使用 try-except - EAFP 原則：先做再說)
    # ---------------------------------------------------------
    # 為什麼不用 if？因為我們無法預知使用者會輸入文字("cat")還是數字("123")。
    # 這裡貫徹「精準防禦」：try 區塊越小越好，只包住可能出錯的那一行。
    try:
        buy = float(sys.argv[1])
    except ValueError:
        # 如果 sys.argv[1] 是字串(例如 "cat")，float() 會引發 ValueError
        sys.exit("\nCommand-line argument is not a number")

    # Transaction(buy) 寫在 try-except 的外面。
    # 這樣可以避免 Transaction 內部的 ValueError 被上面這個 except 誤抓。
    Transaction(buy)


def Transaction(buy):
    # ---------------------------------------------------------
    # 處理不可控的外部環境 (網路請求 API)
    # ---------------------------------------------------------
    try:
        # requests.get 用於向伺服器要資料
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a31b9611b661a2720a95f6570d137f4d4a335bb600daf319004a7b8cbd613fe8")
        # 它的作用是：如果 HTTP 狀態碼不是 200 (例如 404 找不到網頁)，
        # 它會主動幫你拋出一個 HTTPError，讓底下的 except 可以順利抓到它。
        response.raise_for_status()

    except requests.RequestException:
        # requests.RequestException 是所有 requests 模組錯誤的「總稱」。
        # 無論是斷網、逾時、還是 404，都會被這個 except 抓到。
        sys.exit("Network error occurred")

    response_json = response.json()

    # ---------------------------------------------------------
    # API 資料解析與字串格式化 (防範外部資料結構突變)
    # ---------------------------------------------------------
    try:
        # API 回傳的價格可能是字串格式(例如 "77440.81")，必須轉為 float 才能計算。
        price_usd = float(response_json["data"]["priceUsd"])
        result = buy * price_usd

        # - 「,」：加上千分位逗號。
        # - 「.4f」：強制顯示到小數點後 4 位 (float)。
        print(f"${result:,.4f}")
    except (KeyError, ValueError):
        # 1. KeyError：如果有一天 API 改版了，"priceUsd" 這個鍵值不見了。
        # 2. ValueError：如果 API 傳回了無法轉成浮點數的怪異資料。
        # 因為這兩者都屬於「API 資料解析失敗」，所以統整在一起處理是合理的。
        sys.exit("Error parsing price data")

if __name__ == "__main__":
    main()


"""
=============================================================================
💡 PYTHON 防禦性編程與例外處理複習筆記 (Review Notes)
=============================================================================

【一、常見 Exception（例外錯誤）大全】
-----------------------------------------------------------------------------
1. ValueError         : 值無效。當你對不適合的資料進行型態轉換時。
                        -> 解法：用 try-except ValueError 包覆。範例：float("cat")
2. KeyError           : 找不到鑰匙。在字典中查找一個不存在的 Key。
                        -> 解法：確認 Key 沒拼錯或用 .get()。範例：d["b"]
3. IndexError         : 索引超界。存取 List 中不存在的順序位置。
                        -> 解法：操作前先檢查 len()。範例：sys.argv[1] (無參數時)
4. TypeError          : 型態不合。強行把兩種無法混合的型態做運算。
                        -> 解法：確保型態一致。範例："5" + 5
5. EOFError           : 意外中斷。使用者在 input() 時按下 Ctrl + D。
                        -> 解法：用 try-except EOFError 並 sys.exit 退出。
6. ZeroDivisionError  : 除以零。數學運算中分母為 0。
                        -> 解法：計算前先檢查分母 != 0。範例：100 / 0
7. FileNotFoundError  : 檔案遺失。open() 讀取不存在的檔案路徑。
                        -> 解法：確認路徑或用 try-except 保護。範例：open("ghost.txt")


【二、防禦思維：LBYL vs. EAFP】
-----------------------------------------------------------------------------
1. LBYL (Look Before You Leap / 先看再跳)
   - 核心精神：在動手做事之前，先用 if 預先檢查條件，確保安全才執行。
   - 適合情境：結構單純、狀態明確、可輕易預測的內部條件。
   - 範例：檢查參數數量 (if len(sys.argv) < 2: ...)

2. EAFP (Easier to Ask for Forgiveness than Permission / 先做再說，出事再道歉)
   - 核心精神：直接把事情做下去 (放 try 裡)，出錯了再由 except 溫柔接住。
   - 適合情境：面對複雜、不可控的外在環境 (使用者輸入、網路、檔案、API)。
   - 範例：轉型 (try: buy = float(sys.argv[1]) except ValueError: ...)


【三、血淚教訓：為什麼「把字串轉數字」不能用 if 檢查？】
-----------------------------------------------------------------------------
許多初學者會想用 if user_input.isdigit(): 來防範錯誤，但這會踢到大鐵板：
- 負數("-5")     -> .isdigit() 會回傳 False (因為負號不是數字)
- 小數("3.14")   -> .isdigit() 會回傳 False (因為小數點不是數字)
- 科學記號("1e3") -> .isdigit() 會回傳 False

👉 結論：字串千奇百怪，用 if 會漏掉大量邊界狀況 (Edge Cases)。
👉 最佳解：擁抱 EAFP。讓 Python 內建功能 (如 float()) 去解析，因為它懂負數與小數；
   你只需要用 try-except ValueError 把例外接住即可，這是最聰明安全的做法！
=============================================================================
"""