import re
import sys

def main() -> None:
    """Main application entry point.
    
    Prompts the user for a 12-hour time interval, converts it to 24-hour 
    format, and prints the result.
    """
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    """Converts a 12-hour time interval string to its 24-hour equivalent.

    Args:
        s (str): A string representing a time interval in one of the accepted 
                 12-hour formats (e.g., '9:00 AM to 5:00 PM', '9 AM to 5 PM').

    Returns:
        str: The converted time interval in 24-hour format (e.g., '09:00 to 17:00').

    Raises:
        ValueError: If the input string does not match the required format 
                    or contains invalid time values.
    """
    # Strict regex pattern validation:
    # - ^ and $ ensure the entire string matches from start to finish.
    # - Group 1 & 4: Hours (1-12).
    # - Group 2 & 5: Optional minutes (colon followed by 00-59).
    # - Group 3 & 6: Meridian specifier ('AM' or 'PM').
    pattern = r"(^[1-9]|1[0-2])(?::([0-5]?[0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5]?[0-9]))? (AM|PM)$"

    if matches := re.search(pattern, s):

        def parse_time(hour_str: str, minute_str: str | None, ap: str) -> tuple[int:int]:
            """Helper function to parse and convert individual 12-hour time components."""
            h = int(hour_str)
            # Default to 0 minutes if the minute component was omitted in the input.
            m = int(minute_str) if minute_str is not None else 0

            # Apply 12-hour to 24-hour conversion rules:
            # - 12:xx AM corresponds to 00:xx (midnight).
            # - 1:xx ~ 11:xx PM require adding 12 hours to shift into the afternoon/evening cycle.
            if ap == "AM" and h == 12:
                h = 0
            elif ap == "PM" and 1 <= h <= 11:
                h += 12
            return h, m

        # Unpack matched groups and parse both time intervals independently.
        h1, m1 = parse_time(matches.group(1), matches.group(2), matches.group(3))
        h2, m2 = parse_time(matches.group(4), matches.group(5), matches.group(6))

        # Format both times into zero-padded two-digit string representations.
        return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

    # Fail-fast mechanism: raise ValueError if string fails regex pattern matching.
    raise ValueError

        
if __name__ == "__main__":
    main()



"""
=============================================================================
💡 CS50 Python Week 7: working.py 實戰筆記與 12/24 小時制轉換
=============================================================================

【一、 題目核心與驗證目標】
-----------------------------------------------------------------------------
- 任務：撰寫 convert(s) 函式，將 12 小時制的時間區間（例如 "9 AM to 5 PM"）
  轉換為 24 小時制格式（例如 "09:00 to 17:00"）。
- 支援格式：
  1. 9:00 AM to 5:00 PM
  2. 9 AM to 5 PM
  3. 9:00 AM to 5 PM
  4. 9 AM to 5:00 PM
- 防禦邊界：若輸入格式不符、字串前後有多餘字元、或時間數值無效（如 12:60 AM），
  必須主動引發 ValueError。


【二、 核心防禦正則表達式解析】
-----------------------------------------------------------------------------
pattern = r"^(^[1-9]|1[0-2])(?::([0-5]?[0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5]?[0-9]))? (AM|PM)$"

1. ^ 與 $ ：確保整個字串「從頭到尾」完全符合格式，防止前後夾雜多餘垃圾字元。
2. ([1-9]|1[0-2]) ：匹配 1 到 12 的合法小時。
3. (?::([0-5]?[0-9]))? ：選填的分鐘組（冒號加 00 到 59 分），利用非捕捉群組 ?:
   包覆整個冒號，讓內層只捕捉純數字。
4. (AM|PM) ：精準匹配大寫的 AM 或 PM。


【三、 12 小時制轉 24 小時制邏輯清單】
-----------------------------------------------------------------------------
🕒 1. 關於 AM (上午 / Ante Meridiem) 的變化規則：
   - 定義：從「半夜 12 點 (00:00)」到「中午 11:59」。
   - 【12 點開頭 (12:xx AM)】：代表半夜零時，小時必須從 12 變成 00。
     (範例：12:00 AM ➔ 00:00，12:59 AM ➔ 00:59)
   - 【1 到 11 點 (1:xx AM ~ 11:xx AM)】：數字完全不用改變，保持原樣。
     (範例：9:00 AM ➔ 09:00，1:00 AM ➔ 01:00)

🕒 2. 關於 PM (下午 / Post Meridiem) 的變化規則：
   - 定義：從「中午 12 點 (12:00)」到「晚上 11:59」。
   - 【12 點開頭 (12:xx PM)】：正好是中午 12 點正，24 小時制維持 12 不變。
     (範例：12:00 PM ➔ 12:00，12:30 PM ➔ 12:30)
   - 【1 到 11 點 (1:xx PM ~ 11:xx PM)】：下午與晚上時間，小時必須「加上 12」。
     (範例：1:00 PM ➔ 1+12=13 ➔ 13:00，5:00 PM ➔ 5+12=17 ➔ 17:00)


【四、 註解 (Comments) 與文件字串 (Docstrings) 的差別】
-----------------------------------------------------------------------------
寫法：使用 # 開頭。

用途：寫給自己或協作者看的小提醒，解釋某一行或某個區塊「為什麼」要這樣寫。

特點：Python 直譯器執行時會直接忽略它，對程式本身的屬性與 IDE 沒有影響。

文件字串 (Docstrings)

寫法：使用三引號 """  """ 包起來。

用途：作為函式、類別或模組的「官方說明書」，說明這個函式在幹嘛、吃什麼參數（Args）、
回傳什麼（Returns）、會噴什麼錯（Raises）。

特點：Python 會把它當作物件屬性保留（存放在 __doc__ 裡），
當你在 VS Code 把滑鼠懸停在函式上時，彈出來的智慧提示（Tooltip）顯示的就是它。
=============================================================================
"""