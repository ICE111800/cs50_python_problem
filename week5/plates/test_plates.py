"""
單元測試模組：測試 plates.py 中的 is_valid 函式是否符合 CS50 車牌驗證規則。
涵蓋範圍：長度限制、前兩碼字母、數字規則（如 0 開頭與夾雜英文）、型態防禦。
"""

import pytest
from plates import is_valid

@pytest.mark.parametrize("plate, expected", [
    ("a", False),       # 太短 (長度 1)
    ("ab", True),       # 邊界合法 (長度 2)
    ("abcdef", True),   # 邊界合法 (長度 6)
    ("abcdefg", False), # 太長 (長度 7)
    ("", False),        # 空字串
])
def test_length(plate, expected):
    assert is_valid(plate) == expected


@pytest.mark.parametrize("plate, expected", [
    ("AB12", True),     # 前兩碼皆為字母
    ("1A23", False),    # 第一碼是數字
    ("A234", False),    # 第二碼是數字
    ("A", False),       # 單一字母（長度不足會被攔截，但開頭檢查也必須安全）
])
def test_first_two_letters(plate, expected):
    assert is_valid(plate) == expected


@pytest.mark.parametrize("plate, expected", [
    ("AB012", False),   # 數字開頭不能是 0
    ("AB12C", False),   # 數字後面不能夾雜英文字母
    ("AB1234", True),   # 合法數字結尾
    ("ABCDEF", True),   # 全英文合法（無數字）
])
def test_number_rules(plate, expected):
    assert is_valid(plate) == expected


@pytest.mark.parametrize("plate, expected", [
    ("AB!12", False),   # 包含特殊符號
    ("AB 12", False),   # 包含空格
    # (12345, False),     # 【型態防禦測試】傳入整數而不是字串
    # (None, False),      # 【型態防禦測試】傳入 None
])
def test_invalid_chars_and_types(plate, expected):
    assert is_valid(plate) == expected



"""
============================================================
【Python 複習筆記】Pytest 進階技巧與專案最佳實踐
============================================================

1. Pytest 參數化測試 (@pytest.mark.parametrize)
   - 參數命名規則：
     裝飾器字串裡的名稱（例如 "plate, expected"），
     必須與測試函式接收的參數名稱**完全一模一樣**。
   - 活的文件（Living Documentation）：
     每組測試資料後面一定要加上註解（例如 `# 太短`、`# 包含特殊符號`）。
     這能讓測試資料本身具備可讀性，一眼看出在測什麼，避免變成大雜燴。

2. 測試執行方式：一般 Pytest vs 覆蓋率分析
   - `pytest test_plates.py`：
     只負責執行測試，檢查結果是 Pass 還是 Fail。
   - `pytest --cov=plates test_plates.py`：
     除了跑測試，還會進行「程式碼覆蓋率（Code Coverage）」分析，
     告訴你有多少比例的程式碼被測試執行到了（例如 88%），
     幫忙找出漏掉沒測到的盲點。
   - 暫存檔案（如 .pytest_cache/、.coverage）：
     工具自動產生的快取與數據紀錄，不影響程式碼，可安心忽略（通常會加入 .gitignore）。

3. 軟體工程核心觀念：Git 版本控制
   - 金句：「沒有 Commit 的程式碼，等於從來沒存在過。」
   - 標準開發流程：
     本地端開發與測試（綠燈） ➡️ Git 提交（Commit） ➡️ 推送到遠端倉庫備份（Push）。
     確保心血不會因硬體或雲端異常而蒸發。
============================================================
"""