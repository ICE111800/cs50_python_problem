import re
import sys
import time
import yfinance as yf
from datetime import datetime
from loguru import logger
from notifier import send_discord_alert

# 設定日誌格式
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time: YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
    colorize=True
)

class StockMonitor():
    """專業級台灣股票即時監控與分析類別"""

    def __init__(self, stock_code: str) -> None:
        self.pattern = r"(^\d{4}(L|R|B|U|A|T|K)?\.(TW|TWO)$|^00\d{2,4}(L|R|B|U|A|T|K)?\.(TW|TWO)$)"

        if not re.search(self.pattern, stock_code):
            raise ValueError("股票代號格式錯誤！請輸入正確的台股代號！")

        self.stock_code_str = stock_code.upper()
        self.ticker = yf.Ticker(self.stock_code_str)
        self.info: dict = {}

        # 初始化時抓取一次數據進行驗證
        self.refresh_data()

    def refresh_data(self) -> None:
        """向 API 刷新最新市場資料（封裝網路請求，避免重複初始化物件）"""
        try:
            self.info = self.ticker.info
            if not self.info or not any(
                self.info.get(k) is not None for k in ['currentPrice', 'regularMarketPrice', 'previousClose']
            ):
                raise ValueError("找不到此股票代號的有效市場資料！")
        except Exception as e:
            raise ValueError(f"無法取得股票資料: {e}")


    def get_current_price(self) -> float:
        """多重備用價格機制取得最新價"""
        price = (
            self.info.get('currentPrice')
            or self.info.get('regularMarketPrice')
            or self.info.get('previousClose')
        )
        return float(price)


    def analyze_market(self, target_price: float) -> dict:
        """深度金融分析：計算價差百分比、振幅、趨勢與觸發狀態"""
        current_price = self.get_current_price()
        target = float(target_price)

        # 價差百分比（方向性指標）
        gap_percent = ((current_price - target) / target) * 100

        # 標準今日振幅
        day_high = self.info.get('regularMarketDayHigh', current_price)
        day_low = self.info.get('regularMarketDayLow', current_price)
        prev_close = self.info.get('previousClose' , current_price)
        amplitude = ((day_high - day_low) / prev_close) * 100 if prev_close else 0.0

        # 盤勢趨勢
        open_price = self.info.get('regularMarketOpen', current_price)
        trend = "📈 多方強勢 (紅K)" if current_price >= open_price else "📉 空方壓制 (綠K)"

        return {
            "current_price": current_price,
            "gap_percent": round(gap_percent, 2),
            "amplitude": round(amplitude, 2),
            "trend": trend,
            "is_triggered": current_price >= target
        }

        
def main() -> None:
    POLL_INTERVAL = 10  # 輪詢間隔秒數（常數化）

    try:
        stock_code: str = input("請輸入欲監控的股票代碼: ").strip()
        target_price: float = float(input("請輸入您的目標價格: "))

        # 在迴圈外初始化一次物件（避免重複建立與不必要的重複連線驗證）
        monitor = StockMonitor(stock_code)

        logger.info(f"\n🚀 開始即時監控【{stock_code}】 (目標價:{target_price})")
        logger.info("💡 提示：系統每 {POLL_INTERVAL} 秒更新一次，按 Ctrl + C 可隨時終止。\n")
        logger.info("=" * 60)

        # 狀態鎖：用來記錄上一輪是否已經觸發過警報，防止手機被洗版
        was_triggered = False

        while True:
            # 迴圈內僅刷新數據，保持高效能
            monitor.refresh_data()

            analysis = monitor.analyze_market(target_price)
            c_price = analysis["current_price"]
            gap = analysis["gap_percent"]
            is_currently_triggered = analysis["is_triggered"]

            # 終端機顯示狀態
            if is_currently_triggered:
                logger.warning(f"【警報觸發】目前股價 ({c_price}) 已達到或超過目標價 ({target_price})！")
            else:
                logger.info(f"【安全範圍】目前股價 ({c_price}) | 距目標價: {gap:+.2f}% | 振幅: {analysis['amplitude']}% | {analysis['trend']}")

            # 防洗版邏輯：只有當「剛從安全區跨入觸發區」時，才發送 Discord 通知
            if is_currently_triggered and not was_triggered:
                send_discord_alert(
                    stock_code=stock_code,
                    current_price=c_price,
                    target_price=target_price,
                    gap_percent=gap,
                    amplitude=analysis['amplitude'],
                    trend=analysis["trend"],
                    is_triggered=True,
                )
                was_triggered = True    # 鎖定狀態
            elif not is_currently_triggered:
                was_triggered = False   # 如果跌回安全區，解除鎖定，下次突破時可再次通知

            time.sleep(POLL_INTERVAL)

    except ValueError as e:
        logger.error(f"運作失敗: {e}")
    except KeyboardInterrupt:
        sys.exit("\n\n🛑 使用者手動終止監控，系統已安全退出。再見！")

if __name__ == "__main__":
    main()