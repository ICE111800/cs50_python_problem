import sys
from validator_collection import validators, errors

def main():
    """主程式：提示使用者輸入電子郵件，並印出驗證結果。"""
    print(verification_email(input("What's your email address? ")))

def verification_email(input_email:str) -> str:
    """驗證輸入的電子郵件是否合乎語法。
    
    Args:
        input_email (str): 使用者輸入的 Email 字串。
        
    Returns:
        str: 如果合法回傳 "Valid"，不合法則直接透過 sys.exit 結束程式並印出 "Invalid"。
    """
    try:
        # 使用 validator-collection 的 validators.email 進行語法嚴格檢查
        # allow_empty=False 代表不允許空白輸入
        email_address = validators.email(input_email, allow_empty = False)
        return "Valid"
    
    except (errors.InvalidEmailError, ValueError):
        # 如果捕捉到專屬的 Email 格式錯誤，直接印出 Invalid 並終止程式、預防其他可能的數值/格式錯誤
        return "Invalid"
    
    # 如果 try 區塊順利通過且沒有噴錯，代表驗證成功
   

if __name__ == "__main__":
    main()



"""
# Python 學習筆記：Response Validation (電子郵件驗證與第三方庫)

## 一、 核心觀念：為什麼不用自己寫 Regex 驗證 Email？
1. **複雜度極高**：標準的 Email 正規表達式極度冗長且容易出錯。
2. **業界慣例**：對於標準格式（Email、URL、IP），應優先使用 PyPI 上經過社群長期驗證的第三方庫（如 `validators` 或 `validator-collection`），避免造輪子。

## 二、 套件設計模式：Validators vs Checkers
在資料驗證庫中，通常會看到這兩種設計：
- **Validators（驗證器）**：
  - 假設資料「應該是對的」。
  - 驗證成功 ➔ 回傳標準化後的乾淨資料。
  - 驗證失敗 ➔ **直接噴出例外 (Exception)**。
  - *範例*：`validators.email(text)`
- **Checkers（檢查器）**：
  - 單純確認狀態。
  - 不管對錯，**絕對不噴例外**。
  - 僅回傳布林值：`True` 或 `False`。
  - *範例*：`checkers.is_email(text)`
"""
