def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s: str) -> bool:
    # 【型態防禦】如果傳進來的不是字串（例如傳入數字 123、None、或列表），直接防禦性地回傳 False
    if not isinstance(s, str):
        return False

    # 依照 CS50 規範依序檢查：長度 -> 前兩碼 -> 字元合法性 -> 數字規則
    if not text_length(s):
        return False
    if not text_first_two(s):
        return False
    if not only_num_english(s):
        return False
    if not no_letter_after_num(s):
        return False
    
    return True

def text_length(s: str) -> bool:
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def text_first_two(s: str) -> bool:
    if s[:2].isalpha():
        return True
    else:
        return False

def only_num_english(s: str) -> bool:
    if s.isalnum():
        return True
    else:
        return False

def no_letter_after_num(s: str) -> bool:
    # 【關鍵商業邏輯】如果車牌是全英文，沒有數字，直接合法，
    # 避免後面找不到數字索引時發生錯誤。
    if s.isalpha():
        return True
    
    for i, char in enumerate(s):
        if char.isdigit():
            # 規則：數字不能以 '0' 開頭 (例如 CS05 不合法)
            if char == "0":
                return False
            break

    # 確保從第一個數字開始到結尾全部都是數字（後面不能夾雜英文字母）
    if s[i:].isdigit():
        return True
    else:
        return False
    

if __name__ == "__main__":
    main()



"""
============================================================
【Python 複習筆記】車牌驗證專案 (Vanity Plates) 核心觀念總結
============================================================

1. 型態防禦（Type Checking）與 isinstance()
   - 概念：防範非預期型態（如 int, None, list）導致程式崩潰。
   - 內建函式 isinstance(變數, 型態)：
     用來安全地檢查變數是否為指定型態。
   - 範例寫法（放在函式最開頭）：
     if not isinstance(s, str):
         return False

2. 型態提示（Type Hinting）
   - 概念：在函式簽章中明確宣告參數與回傳值的型態。
   - 業界標準：現代專案普遍使用，能提供 IDE 語法檢查與自我文件化。
   - 範例：
     def is_valid(s: str) -> bool:
         ...

3. 程式碼風格：防衛式條款（Guard Clauses）
   - 概念：當條件不符時直接 return，避免多層巢狀縮排（if/elif/else）。
   - 優點：結構扁平、像安檢門一樣一關一關過，可讀性極高。
   - 範例：
     if not text_length(s):
         return False
     if not text_first_two(s):
         return False
     return True

4. Pytest 進階技巧：參數化測試 (@pytest.mark.parametrize)
   - 概念：將測試資料表格化，避免寫一堆重複的 assert。
   - 模組化最佳實踐：
     不要把所有測試全部塞在同一個清單裡成大雜燴。
     應按「功能模組 / 錯誤情境」拆分多個短小的測試函式：
     * test_length()       -> 專門測長度邊界
     * test_first_two()    -> 專門測開頭兩碼字母
     * test_number_rules() -> 專門測數字規則與 0 開頭
     * test_invalid_types() -> 專門測特殊符號與型態防禦
   - 優點：報錯時能秒速定位是哪一個商業邏輯維度出問題！
============================================================
"""



"""
============================================================
【Python 複習筆記】註解的藝術與測試檔案的最佳實踐
============================================================

1. 程式碼註解的黃金原則（How & When to Comment）
   - ❌ 錯誤示範（流水帳註解）：
     每一行都用中文翻譯程式碼（例如 `# 檢查長度是不是小於 6`）。
     缺點：製造視覺垃圾，程式碼本身已經夠易讀時，註解多餘且難維護。
   - ⭕ 正確示範（解釋 Why，而不是 What）：
     只在「有特殊商業規則」、「非直覺邏輯」或「防禦性黑魔法」的地方下註解。
     例如解釋為什麼要先特判 `s.isalpha()`，避免後面索引報錯。

2. 單元測試檔案（test_plates.py）的黃金標準結構
   - 檔案最頂部（Module-level Docstring）：
     加上一段簡單的模組說明，交代這個測試檔案是用來測什麼、涵蓋哪些維度。
   - 測試函式命名：
     以功能模組命名（如 test_length、test_number_rules），一眼看出測試範圍。
   - 行內註解（Living Documentation）：
     在參數化測試的資料後面加上精準註解（如 `# 0 開頭`、`# 型態防禦`），
     讓測試數據本身變成活的文件，不需要去看程式碼邏輯就能懂測試目的。
============================================================
"""