def main():
    # 使用 while True 建立無限迴圈，確保輸入錯誤時能持續「重新提示」使用者
    while True:
        try:
            # 取得輸入並去除前後空白
            date = input("Date: ").strip()

            # 判斷是哪一種格式並處理
            if "/" in date:
                Separate_Format_Slash(date)
                break 
            elif "," in date:
                Separate_Format_Comma(date)
                break
            else:
                # 如果既沒有斜線也沒有逗號，不符合兩種格式，手動引發錯誤
                raise ValueError

        # =========================================================
        # 【資料驗證型的 Try-Except 範圍】
        # 這裡將整個解析與轉換流程包在裡面：
        # 不論是 int() 轉型失敗、月份拼錯字導致 IndexError、
        # 或是我們手動 raise ValueError，全部都會被這裡精準攔截。
        # 攔截後程式不會當掉，而是靜默 pass，讓 while 迴圈自動重新要求 input()
        # =========================================================
        except (ValueError, IndexError):
            pass
     
        
        
def Separate_Format_Slash(date):
    # 以斜線 "/" 將字串切割成清單 (例如: "9/8/1636" -> ["9", "8", "1636"])
    part = date.split("/")

    # 防呆機制：如果切出來的長度不等於 3 (代表格式不對)，引發錯誤
    if len(part) != 3:
        raise ValueError

    # 將切割出來的字串轉成整數
    month = int(part[0])
    day = int(part[1])
    year = int(part[2])

    # 檢查邏輯範圍是否合法 (月份 1~12，日期 1~31，年份 >= 0)
    if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
        # 使用 f-string 格式化規格印出：
        # :04 代表年份不足 4 位數左邊補 0
        # :02 代表月份與日期不足 2 位數左邊補 0 (符合 ISO 8601 標準)
        print(f"{year:04}-{month:02}-{day:02}")
    else:
        raise ValueError


def Separate_Format_Comma(date):
    # 定義標準的英文月份清單 (用來將英文名字對應成數字)
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # 移除逗號：把 "," 換成空字串 "" (例如: "September 8, 1636" -> "September 8 1636")
    date = date.replace(",","")

    # # 改用不帶參數的 .split()，自動處理所有空白與多重空格
    # 切割成清單 -> ["September", "8", "1636"]
    part = date.split("")
    if len(part) != 3:
        raise ValueError
    
    month_name = part[0]

    # 確保月份名稱確實存在於清單中，否則直接引發錯誤
    if month_name not in months:
        raise ValueError

    # 取得月份數字：
    # .index(month_name) 去 months 清單找這個英文名字的索引位置 (從 0 開始)
    # + 1 是因為人類月份從 1 開始算，而電腦索引從 0 開始
    # (如果月份打錯字，.index() 會找不到並報錯，剛好被外層 try-except 抓到)
    month = int(months.index(month_name) + 1)
    day = int(part[1])
    year = int(part[2])

    if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
        print(f"{year:04}-{month:02}-{day:02}")
    else:
        ValueError

if __name__ == "__main__":
    main()