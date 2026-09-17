import io
import json
import os
from dotenv import load_dotenv
from loguru import logger
import matplotlib.pyplot as plt
import requests
import yfinance as yf

# 載入 .env 檔案
load_dotenv()

# 改用 os.getenv 安全獲取網址
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def generate_stock_chart(stock_code: str) -> io.BytesIO:
    """自動抓取歷史數據並繪製趨勢圖，將圖片以二進位流存入記憶體中（避免硬碟殘留與 IO 瓶頸）"""
    try:
        ticker = yf.Ticker(stock_code)
        hist = ticker.history(period="5d")

        if hist.empty:
            raise ValueError(f"無法取得 [{stock_code}] 的歷史數據來繪製圖表。")
        
        # 建立畫布與座標系
        fig, ax = plt.subplots(figsize = (8, 4))
        ax.plot(
            hist.index,
            hist['Close'],
            label='Close Price',
            color = '#2b5c8f',
            linewidth = 2,
            marker ='o',
            markersize = 3
        )
        ax.set_title(f"[{stock_code}] Recent Price Trend (5D)", fontsize=14, fontweight='bold')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.grid(True, linestyle = '--', alpha = 0.6)
        plt.tight_layout()

        # 將圖片存入記憶體緩衝區（不佔用硬碟空間）
        buf = io.BytesIO()
        plt.savefig(buf, format = 'png', dpi = 150)
        buf.seek(0) # 指標歸零，供後續網路請求讀取
        plt.close(fig)  # 強制關閉畫布，防止記憶體洩漏 (Memory Leak)

        return buf
    
    except Exception as e:
        logger.error(f"圖表生成失敗: {e}")
        raise


def send_discord_alert(
    stock_code: str,
    current_price: float,
    target_price: float,
    gap_percent: float,
    amplitude: float,
    trend: str,
    is_triggered: bool
) -> None:
    """發送帶有 Embed 嵌入式卡片與即時走勢圖的 Discord 警報通知"""

    if not is_triggered:
        return  # 未觸發則直接返回，避免手機被安全訊息洗版

    logger.info("📊 正在生成即時股價趨勢圖...")

    try:
        chart_buf = generate_stock_chart(stock_code)
    except Exception:
        logger.error("❌ 略過此次通知：因圖表生成失敗無法發送圖片卡片。")
        return

    # 構築 Discord 結構化卡片 (Embeds)
    payload = {
        "embeds": [
            {
                "title": "🚨 【股市警報觸發通知】",
                "color": 16711680,  # 鮮紅色邊框，代表高度警告
                "fields": [
                    {"name": "📌 監控標的", "value": f"{stock_code}", "inline": True},
                    {"name": "🎯 設定目標價", "value": f"{target_price}", "inline": True},
                    {"name": "💰 目前成交價", "value": f"{current_price}", "inline": True},
                    {"name": "📊 價差幅度", "value": f"{gap_percent:+.2f}%", "inline": True},
                    {"name": "🌊 今日振幅", "value": f"{amplitude}%", "inline": True},
                    {"name": "📈 盤勢趨勢", "value": f"{trend}", "inline": False}
                ],
                "image": {
                    "url": "attachment://stock_trend.png"   # 綁定 multipart 上傳的檔案代號
                },
                "footer": {
                    "text": "Tw Market Monitor System | CS50P Project"
                }
            }
        ]
    }

    # 準備 multipart/form-data 格式的檔案與資料 (將記憶體中的圖片命名為 stock_trend.png)
    files = {
        'file0': ('stock_trend.png', chart_buf, 'image/png')
    }

    # 傳送帶有圖片的複合式請求
    data = {
        'payload_json': json.dumps(payload)
    }

    try:
        response = requests.post(WEBHOOK_URL, data=data, files=files, timeout=10)
        if response.status_code == 200:
            logger.info("🖼️ Discord 專業圖表警報推播發送成功！")
        else:
            logger.error(f"💬 Discord 推播失敗，狀態碼: {response.status_code}, 內容: {response.text}")
    except Exception as e:
        logger.error(f"💬 Discord 推播發生錯誤: {e}")

if __name__ == "__main__":
    # 獨立模組測試：可直接執行 python notifier.py 測試圖表與 Webhook 是否正常
    print("🧪 正在進行 notifier.py 獨立測試推播...")
    send_discord_alert(
        stock_code="2330.TW",
        current_price=1050.0,
        target_price=1000.0,
        gap_percent=5.0,
        amplitude=2.45,
        trend="📈 多方強勢 (紅K)",
        is_triggered=True
    )