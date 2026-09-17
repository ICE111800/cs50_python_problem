import pytest
from numb3rs import validate

# 測試正常數值
@pytest.mark.parametrize("ip, expected", [
    ("1.1.1.1", True),
    ("164.159.164.159", True),
    ("255.255.255.0", True),
    ("101.0.150.80", True),
])
def test_normal_ip(ip, expected):
    assert validate(ip) == expected

# 測試 0 開頭 (前導零)
@pytest.mark.parametrize("ip, expected", [
    ("0.55.55.1", True),
    ("101.011.101.11", False),
    ("50.10.050.29", False),
    ("43.27.1.003", False),
])
def test_start_zero_ip(ip, expected):
    assert validate(ip) == expected

# 測試英文字母集各種符號的輸入
@pytest.mark.parametrize("ip, expected", [
    ("a.b.c.d", False),
    ("A.B.C.D", False),
    ("_.^.!.?", False),
    ("a.10.10.20", False),
    ("11.B.20.30", False),
    ("20.20.C.30", False),
    ("40.50.60.d", False),
])
def test_symbols_and_letters(ip, expected):
    assert validate(ip) == expected

# 測試邊界值與數位異常
@pytest.mark.parametrize("ip, expected", [
    ("255.255.255.255", True),  # 最大邊界
    ("256.1.1.1", False),       # 超過 255
    ("1.1.1.256", False),       # 結尾超過 255
    ("-1.1.1.1", False),        # 負數
    ("1.2.3", False),           # 區段太少
    ("1.2.3.4.5", False),       # 區段太多
    (" 1.2.3.4 ", False),       # 帶有空白
    ("", False),                # 空字串
])
def test_edge_cases(ip, expected):
    assert validate(ip) == expected