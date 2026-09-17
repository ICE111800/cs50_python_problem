from unittest.mock import patch
import pytest
from project import StockMonitor


# 1. 建立測試用的標準假資料（Mock Data），避免單元測試受網路影響
@pytest.fixture
def mock_ticker_info():
    return {
        "shortName": "Taiwan Semiconductor Manufacturing Company Limited",
        "currency": "TWD",
        "marketState": "REGULAR",
        "currentPrice": 1050.0,
        "regularMarketPrice": 1050.0,
        "regularMarketChange": 20.0,
        "regularMarketChangePercent": 1.94,
        "regularMarketOpen": 1030.0,
        "regularMarketDayHigh": 1060.0,
        "regularMarketDayLow": 1025.0,
        "regularMarketVolume": 25000000,
        "previousClose": 1030.0,
    }


@patch("project.yf.Ticker")
def test_stock_monitor_init_valid(mock_ticker_class, mock_ticker_info):
    """測試合法的台灣股票代號是否能成功初始化物件"""
    # 攔截 yf.Ticker，讓它回傳我們的假資料，不實際發動網路請求
    mock_instance = mock_ticker_class.return_value
    mock_instance.info = mock_ticker_info

    monitor = StockMonitor("2330.TW")
    assert monitor.stock_code_str == "2330.TW"


@pytest.mark.parametrize(
        "invalid_code",
        [
            "1234",     # 少了市場尾綴 (.TW / .TWO)
            "2330.US",  # 錯誤的市場代號
            "ABC.TW",   # 英文代號格式錯誤
            "2330.tw",  # 小寫格式（正則要求大寫）
            "0050",     # 缺少市場區辨
        ],
)
def test_stock_monitor_init_invalid(invalid_code):
    """使用參數化測試 (Parametrize) 驗證不合法的股票代號是否會正確引發 ValueError"""
    with pytest.raises(ValueError):
        StockMonitor(invalid_code)


@patch("project.yf.Ticker")
def test_analyze_market_triggered(mock_ticker_class, mock_ticker_info):
    """測試當現價達到或超過目標價時，分析結果是否正確顯示觸發狀態與價差百分比"""
    mock_instance = mock_ticker_class.return_value
    mock_instance.info = mock_ticker_info   # 現價設定為 1050.0

    monitor = StockMonitor("2330.TW")
    # 設定目標價為 1000.0 (現價 1050 >= 1000，應觸發)
    analysis = monitor.analyze_market(target_price=1000.0)

    assert analysis["current_price"] == 1050.0
    assert analysis["is_triggered"] is True
    # 驗證價差公式: ((1050 - 1000) / 1000) * 100 = 5.0%
    assert analysis["gap_percent"] == 5.0


@patch("project.yf.Ticker")
def test_analyze_market_safe(mock_ticker_class, mock_ticker_info):
    """測試當現價低於目標價時，分析結果是否為未觸發狀態"""
    mock_instance = mock_ticker_class.return_value
    mock_instance.info = mock_ticker_info   # 現價設定為 1050.0

    monitor = StockMonitor("2330.TW")
    # 設定目標價為 1100.0 (現價 1050 < 1100，應未觸發)
    analysis = monitor.analyze_market(target_price=1100.0)

    assert analysis["is_triggered"] is False
    # 驗證價差公式: ((1050 - 1100) / 1100) * 100 = -4.55%
    assert analysis["gap_percent"] == -4.55


@patch("project.yf.Ticker")
def test_analyze_market_trend_and_amplitude(mock_ticker_class, mock_ticker_info):
    """測試盤勢趨勢 (多空判斷) 與今日振幅計算邏輯是否正確"""
    mock_instance = mock_ticker_class.return_value
    mock_instance.info = mock_ticker_info
    # 假資料中: currentPrice=1050, regularMarketOpen=1030 (1050 >= 1030 應為多方強勢)

    monitor = StockMonitor("2330.TW")
    analysis = monitor.analyze_market(target_price=1000.0)

    assert "多方強勢" in analysis["trend"]

    # 驗證振幅計算公式: ((day_high - day_low) / prev_close) * 100
    # ((1060 - 1025) / 1030) * 100 = (35 / 1030) * 100 = 3.40%
    assert analysis["amplitude"] == 3.40

