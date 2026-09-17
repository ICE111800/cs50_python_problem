import pytest
from um import count

# 正常情況測試（涵蓋大小寫、標點符號、前後空白）
@pytest.mark.parametrize("text, expected", [
    ("hello, um, world", 1),
    ("um", 1),
    ("um?", 1),
    ("Um, thanks for the album.", 1),
    ("Um, thanks, um...", 2),
    (" um ", 1),
])
def test_normal(text, expected):
    """測試各種合法且應被計數的 um 輸入"""
    assert count(text) == expected

# 邊界與子字串測試（確保 um 不是其他單字的一部分，防範黏連或變形）
@pytest.mark.parametrize("text, expected", [
    ("yummy", 0),               # um 是 yummy 的子字串
    ("album", 0),               # um 在 album 結尾但不是獨立單字
    ("hello, u.m, world", 0),   # 中間被點隔開
    ("U/m", 0),                 # 被斜線隔開
    ("?u?m?", 0),               # 被問號包圍
    ("uyyuymu", 0),             # 拼湊字
    ("umUMuMUm", 0),            # 連續黏在一起的字母（沒有獨立邊界）
])
def test_error_subwords(text, expected):
    """測試包含 um 但由於不是獨立單字或格式錯誤而應被忽略的輸入"""
    assert count(text) == expected

# 符號、空白異常
@pytest.mark.parametrize("text, expected", [
    ("wow", 0),     # 完全無關的單字
    ("", 0),        # 空字串
    ("  ", 0),      # 純空白
    ("!^.|", 0),    # 純特殊符號
    ("1234", 0),    # 純數字
])
def test_symbol_and_blank(text, expected):
    """測試空字串、純空白、標點符號與無關字串"""
    assert count(text) == expected