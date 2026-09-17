import sys
from random import choice
from pyfiglet import Figlet

def main():
    # 初始化 pyfiglet 物件並取得系統中所有支援的字體清單
    figlet = Figlet()
    font_list = figlet.getFonts()

    # 情況一：使用者未輸入額外參數（僅執行 python figlet.py）
    if len(sys.argv) == 1:
        # 從可用字體清單中隨機挑選一個
        random_font = choice(font_list)
        # 設定字體（注意：setFont 是直接修改物件，不要用變數去接它）
        figlet.setFont(font=random_font)

    # 情況二：使用者輸入了三個參數（python figlet.py -f 字體名稱）
    # 這裡利用全用 and 連接的特性與「短路求值」，確保先檢查長度為 3，
    # 才去安全地檢查 sys.argv[1] 和 sys.argv[2]，絕對不會發生 IndexError！
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in font_list:
        # 將字體設定為使用者指定的字體
        figlet.setFont(font=sys.argv[2])

    # 情況三：其他不符合規定的參數數量或錯誤輸入，直接報錯並終止程式
    else:
        sys.exit("Invalid usage")

    # 防禦性編寫：使用 try-except 攔截使用者在 input 時按下 Ctrl+D (EOFError)
    try:
        text = input("Input: ").strip()
    except EOFError:
        sys.exit("\nExiting program.")

    # 使用 figlet 將文字轉換成 ASCII 藝術字體並印出
    print(f"Output: \n{figlet.renderText(text)}")

if __name__ == "__main__":
    main()