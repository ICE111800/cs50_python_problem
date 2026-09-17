import re
import sys


def main():
    """主程式：提示使用者輸入文字，並印出 um 出現的次數。"""
    print(count(input("Text: ")))


def count(s: str) -> int:
    """計算字串中「獨立且不分大小寫」的單字 um 出現次數。
    
    Args:
        s (str): 要檢查的輸入文字。
        
    Returns:
        int: um 出現的次數。
    """
    # 定義正規表達式模式：
    # \b 代表單字邊界 (Word Boundary)，確保 um 是一個獨立的單字，
    # 而不會抓到像是 yummy 或 album 這種包含 um 的子字串。
    pattern = r"\b(um)\b"
    # 使用 re.findall 尋找所有符合 pattern 的項目，並加入 re.IGNORECASE 忽略大小寫
    matches = re.findall(pattern, s, re.IGNORECASE)

    # 回傳找到的總數量（串列的長度）
    return len(matches)


if __name__ == "__main__":
    main()