import pytest
from datetime import date
from seasons import get_birth_date, calculate_minutes, convert_num_to_text

# ============================================================
# 1. 測試 get_birth_date（日期格式解析與驗證）
# ============================================================

@pytest.mark.parametrize("birth_str, expected_date", [
    ("1990-01-01", date(1990, 1, 1)),
    ("0001-12-31", date(1, 12, 31)),
    ("2024-02-29", date(2024, 2, 29)),  # 測試閏年合法日期
])
def test_get_birth_date_success(birth_str, expected_date):
    """測試合法的 YYYY-MM-DD 格式是否能正確回傳對應的 date 物件"""
    assert get_birth_date(birth_str) == expected_date


# 測試異常 get_birth_date
@pytest.mark.parametrize("invalid_birth", [
    "100-01-01",          # 年份位數錯誤
    "1900-4-10",          # 月份位數錯誤
    "1895-05-2",          # 日期位數錯誤
    "-100-10-10",         # 負數年份
    "2100-13-10",         # 不存在的月份 (13月)
    "2000-12-32",         # 不存在的日期 (32日)
    "2023-02-29",         # 2023 不是閏年，沒有 2月29日
    "January 1, 1999",    # 英文格式錯誤
    "20191204",           # 缺少連字號
    "abcd-ef-gh",         # 英文字母格式錯誤
])
def test_get_birth_date_failure(invalid_birth):
    """測試非法的日期格式或數值，是否會透過 sys.exit 觸發 SystemExit 例外"""
    # 註解：因為程式碼中使用 sys.exit()，在 pytest 中會引發 SystemExit，而不是 ValueError
    with pytest.raises(SystemExit):
        get_birth_date(invalid_birth)


# ============================================================
# 2. 測試 calculate_minutes（計算相差分鐘數）
# ============================================================

# 測試正常 calculate_minutes
@pytest.mark.parametrize("birth, present, expected_minutes", [
    # 剛好一年（平年 365 天：365 * 24 * 60 = 525,600
    (date(2025, 9, 7), date(2026, 9, 7), 525600),
    # 包含閏年的一年（2024 是閏年 366 天：365 * 24 * 60 = 525,600 + 366 * 24 * 60 = 527,040）
    (date(2023, 9, 7), date(2025, 9, 7), 1052640),
])
def test_calculate_minutes_success(birth, present, expected_minutes):
    """測試給定兩個 date 物件，是否能正確計算出總分鐘數"""
    assert calculate_minutes(birth, present) == expected_minutes


# ============================================================
# 3. 測試 convert_num_to_text（數字轉英文單字）
# ============================================================

@pytest.mark.parametrize("minutes, expected_text", [
    (525600, "Five hundred twenty-five thousand, six hundred minutes"),
    (1000, "One thousand minutes"),
])
def test_convert_num_to_text_success(minutes, expected_text):
    """測試數字是否能正確轉換為首字母大寫的英文單字，並結尾帶有 minutes"""
    assert convert_num_to_text(minutes) == expected_text


def test_convert_num_to_text_no_and():
    """測試轉換結果中絕對不能包含 ' and'（符合題目的特別要求）"""
    # 65214 在英文拼寫中通常會帶有 and，但inflect設定 andword="" 後應被移除
    result = convert_num_to_text(65214)
    assert " and" not in result
