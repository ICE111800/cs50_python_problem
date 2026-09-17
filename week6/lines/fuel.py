"""
燃料計量模組 (Fuel Gauge)
負責將分數格式的字串轉換為百分比，並根據數值轉換為對應的油量顯示字串。
"""

def main() -> None:
    # "主程式：負責與使用者互動，取得正確的油量並顯示結果。
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            output = gauge(percentage)
            print(output)
            break
        except (ValueError, ZeroDivisionError):
            # 當轉換或計算出錯時，不中斷程式，而是要求使用者重新輸入
            pass

def convert(fraction: str) -> int:
    """
    將 X/Y 格式的分數轉換為 0 到 100 之間的整數百分比。
    若格式錯誤、分子分母非整數、分子大於分母則引發 ValueError。
    若分母為 0 則引發 ZeroDivisionError。
    """
    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError

    
    x = int(parts[0])
    y = int(parts[1])
    

    # 【重要防禦順序】必須先檢查分母是否為 0，否則會先觸發算術崩潰
    if y == 0:
        raise ZeroDivisionError

    # 商業邏輯檢查：分子不能小於 0，且不能大於分母
    if x < 0 or x > y:
        raise ValueError

    # 計算四捨五入的整數百分比
    percentage = round((x / y) * 100)
    return percentage

def gauge(percentage: int) -> str:
    if 1 >= percentage >= 0:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()



"""
============================================================
【Python 複習筆記】異常處理 (Exceptions) 與測試邊界觀念
============================================================

1. ValueError vs TypeError 的核心差異
   - TypeError (型態錯誤)：
     資料「型態」本身就不對，無法執行該操作。
     (例：整數沒有長度，`len(123)` 會噴 TypeError)
   - ValueError (數值/內容錯誤)：
     資料「型態」是對的，但「內容」無法被解析。
     (例：字串轉整數 `int("abc")`，型態是 str 沒錯，但內容 "abc" 無法變成數字，會噴 ValueError)

2. 異常處理三兄弟：try、except、raise (老闆與員工的比喻)
   - raise (拋出炸彈 / 報警)：
     發現不合理的狀況（如分母為 0），主動製造一個錯誤丟出去。
   - try (架設防護網)：
     預期這段程式碼可能會爆炸，在此處張開網子試著執行。
   - except (接住炸彈並善後)：
     如果 try 裡面真的炸了，把錯誤攔下來處理，防止整支程式當機。

3. 錯誤向上傳遞 (Bubble Up)
   - 函數如果沒有寫 try...except，遇到錯誤時，炸彈會「往上丟」給呼叫它的地方。
   - 實務設計：基層函數 (如 convert) 遇到錯只負責 `raise` (丟炸彈)，
     讓最外層的經理 (如 main) 的 `try...except` 統一接住並要求重新輸入。

4. 測試預期錯誤：with pytest.raises()
   - `with` 叫做「內容管理員 (Context Manager)」，幫忙自動防護或善後。
   - 寫法：
     with pytest.raises(ValueError):
         convert("a/1")
   - 意思：「我預期下一行代碼會炸出 ValueError！如果有炸出來，測試就通過 (Pass)；沒炸出來反而算測試失敗。」

5. 職責分離 (Separation of Concerns) 與測試邊界
   - 第一道防線 (對外)：
     直接接收使用者亂七八糟的輸入（如 `convert`），需要做最嚴格的防禦與測試 (測字母、符號、空字串)。
   - 第二道防線 (對內)：
     內部合作的函數（如 `gauge`），因為已經有前人把關，它預期只會收到合法格式（0~100 的 int），
     所以只需測試商業邏輯的「邊界值」(0, 1, 99, 100)，不需再重複測試奇怪的符號字串。
============================================================
"""