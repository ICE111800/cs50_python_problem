import pytest
from fuel import convert, gauge

# 測試正常數值轉換
@pytest.mark.parametrize("division, expected", [
    ("3/6", 50),                            # 正常數字長度
    ("1/4", 25),
    ("0/5", 0),
    ("5/5", 100),
])
def test_convert_success(division, expected):
    assert convert(division) == expected

# 測試各種會引發 ValueError 的錯誤格式
@pytest.mark.parametrize("division", [
    ("a/1"),    # 包含字母
    ("3/3/3"),  # 多個斜線
    ("/"),      # 只有斜線
    (""),       # 空字串
    ("1/"),     # 缺少分母
    ("/3"),     # 缺少分子
    ("-1/5"),   # 分子小於 0
    ("5/2"),    # 分子大於分母
])
def test_convert_value_error(division):
    with pytest.raises(ValueError):
        convert(division)


# 測試除以 0 的 ZeroDivisionError
def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")


# 測試 gauge 函式的燃料顯示規則
@pytest.mark.parametrize("percentage, expected", [
    (0, "E"),
    (1, "E"),
    (2, "2%"),
    (50, "50%"),
    (98, "98%"),
    (99, "F"),
    (100, "F"),
])
def test_gauge(percentage, expected):
    assert gauge(percentage) == expected



"""
============================================================
【Python 複習筆記】Pytest 參數化測試的常見誤區與運作機制
============================================================

1. 為什麼會報「參數數量不對 (number of names vs values)」的錯誤？
   - 這發生在 pytest 收集資料階段，與你的程式碼邏輯（如 split）無關。
   - 原因：
     如果在裝飾器裡宣告了 2 個變數（如 `"division, expected"`），
     但清單裡卻只放一個字串（如 `"a/1"`），
     Python 把它當成可迭代物件去拆解，結果拆出 3 個字元（'a', '/', '1'），
     導致數量兜不攏而報錯。
   - 解決原則：
     裝飾器內的參數變數個數，必須與清單中每個項目提供的數值個數**完全一致**。
     如果只測單一輸入且預期會噴錯，參數宣告 1 個即可。

2. 裝飾器（@pytest.mark.parametrize）怎麼知道是給哪個函式用的？
   - **一對一緊密綁定**：
     Python 的裝飾器永遠**只屬於緊接在它正下方的那個函式**。
   - 運作方式：
     pytest 掃描到裝飾器後，會把清單裡的每一組資料自動帶入下方的函式中，
     迴圈執行對應次數，絕不會跑到其他函式去。
============================================================
"""