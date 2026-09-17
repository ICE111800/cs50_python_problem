def main():
    total = float(0.0)
    while True:
        try:
            # # 只把「可能接收到 EOF (Ctrl+D)」的這行包在 try 裡面
            item = input("Item: ").strip().lower().title()

        # ==========================================
        # 【例外處理 (Try-Except)】
        # 用途：處理「無法控制的系統級外部突發狀況」
        # 例如：使用者按下 Ctrl+D (EOFError)，這是環境訊號，
        # 不是使用者打錯字，所以必須用 try-except 攔截並安全離開。
        # ==========================================
        except EOFError:
            print()
            break

        # 剩下的商業邏輯放在 try 外面，乾淨又直覺
        price = Calculate(item)
        if price > 0:
            total += price
            print(f"${total:.2f}")

        

def Calculate(item):
    products = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # ==========================================
    # 【預期內的商業邏輯 (Business Logic)】
    # 用途：處理「使用者點了不在菜單上的品項（打錯字）」
    # 這在點餐系統裡是「每天都會發生的正常情況」，
    # 我們用字典的 .get(item, 0) 來溫和處理：
    # 找得到就回傳價格，找不到就回傳 0，讓金額維持不變，
    # 絕對不把它們當作「程式錯誤 (Exception)」來抓！
    # ==========================================
    # .get() 的意思是「去字典找這個 key，如果找不到，就給我後面指定的預設值 0」。
    return products.get(item, 0)

if __name__ == "__main__":
    main()