import inflect
import re
import sys
from datetime import date

p = inflect.engine()

def main():
    # 提示使用者輸入並取得驗證後的 date 物件
    birth_date = get_birth_date(input("Date of Birth: "))

    # 計算分鐘數
    minutes = calculate_minutes(birth_date, date.today())

    # 轉換成英文單字並印出
    output_word = convert_num_to_text(minutes)
    print(output_word)


def get_birth_date(birth: str) -> date:
    """驗證格式並回傳 date 物件，格式錯誤則利用 sys.exit 結束"""
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.search(pattern, birth):
        try:
            return date.fromisoformat(birth)
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")

def calculate_minutes(birth_date: date, present_date: date) -> int:
    """計算兩個日期之間相差的總分鐘數"""
    delta = present_date - birth_date
    # delta.days 是總天數，一天有 24*60 分鐘
    return delta.days * 24 * 60

def convert_num_to_text(minutes: int) -> str:
    """將數字轉換為英文單字，並加上 minutes 結尾"""
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()