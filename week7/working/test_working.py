import pytest
from working import convert

# 正常時間輸入
@pytest.mark.parametrize("time, expected", [
    ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
    ("9 AM to 5 PM", "09:00 to 17:00"),
    ("9:00 AM to 5 PM", "09:00 to 17:00"),
    ("9 AM to 5:00 PM", "09:00 to 17:00"),
    ("10 PM to 1 AM", "22:00 to 01:00"),
])
def test_success_time(time, expected):
    assert convert(time) == expected

# 各種異常測試（改用 pytest.raises 來捕捉 ValueError）
@pytest.mark.parametrize("time", [
    ("9:60 AM to 5:60 PM"),     # 分鐘數超過59
    ("9 AM - 5 PM"),            # 字串格式"-"錯誤 
    ("09:00 AM - 17:00 PM"),    # 字串格式"-"錯誤 
    (""),                       # 空字串（補上 ValueError 成對格式）
    ("13:00 AM to 17:00 PM"),   # AM 小時超出範圍
    ("13:00 AM to 25:00 PM"),   # PM 小時超出範圍
    ("9:50 am to 5:50 PM"),     # am 小寫
    ("9:50 AM to 5:50 pm"),     # pm 小寫
    ("9:00 AM to 5:00 PM to 8:00 PM"),  # 格式過長或多餘字元
])
def test_fail_time(time):
    with pytest.raises(ValueError):
        convert(time)



"""
=============================================================================
💡 PYTHON 資源管理與例外處理：從 try...finally 到 with 語法的演進
=============================================================================

【一、 核心概念：為什麼需要「有始有終」的善後機制？】
-----------------------------------------------------------------------------
在寫程式時，常遇到以下情境：
1. 【資源佔用】：開了檔案、資料庫連線或網路 socket，如果用完忘記關閉，
   會導致系統資源洩漏 (Resource Leak)。
2. 【例外中斷】：當程式執行到一半突然噴錯崩潰，後續的清理程式碼如果被跳過，
   就會出大問題。
為了確保「無論過程順利還是半路出錯，善後工作都一定會被執行」，我們需要機制來處理。


【二、 傳統作法一：try...finally (處理資源清理與防護)】
-----------------------------------------------------------------------------
如果不使用 `with` 語法，手動管理資源必須依賴 `try...finally`。
無論 `try` 區塊裡面發生什麼錯誤，`finally` 區塊裡的程式碼「一定會被執行」。

- 範例（手動關閉檔案）：
  ```python
  f = open("example.txt", "w", encoding="utf-8")
  try:
      f.write("Hello, World!")
      # 假設這裡突然發生了未預期的錯誤（例如除以零）
      x = 1 / 0 
  finally:
      # 無論上面有沒有報錯、有沒有當機，finally 都一定會執行
      f.close()
      print("檔案已安全關閉")
-缺點：程式碼冗長，每次開檔案都要寫一整串，工程師容易忘記寫 finally。


【三、 現代 Python 的救星：with 語法 (上下文管理器 Context Manager)】
with 把繁瑣的 try...finally 封裝在幕後，化身為「貼心的管家」：

【進場前 (Setup)】：自動幫你準備好資源（如開檔案）。

執行中 (Action)：執行縮排內的程式碼。

【離場後 (Teardown)】：不管成功或半路當掉，自動幫你善後（如關閉檔案）。

範例（優雅開檔案）：

Python
# 離開 with 區塊時，Python 會自動幫你執行 f.close()，絕對不會忘記！
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")

    
【四、 傳統作法二：try...except (手動捕捉例外與測試)】
在寫單元測試（如 Pytest）時，如果想驗證「這段程式碼有沒有如預期噴出錯誤」，
傳統上必須用 try...except 手動捕捉：

範例（手動測試例外）：

Python
def test_fail_manual():
    try:
        convert("invalid_time")
        # 如果程式跑到這裡，代表它「沒有」如預期噴出錯誤，需手動判定失敗
        pytest.fail("本該噴出 ValueError，但卻沒有發生")
    except ValueError:
        # 順利抓到預期的例外，測試通過 (Pass)
        pass

          
【五、 終極簡化：with pytest.raises()】
Pytest 利用了 with（上下文管理器）的特性，把上述冗長的 try...except 封裝成一行：

範例：

Python
def test_fail_time(time):
    # with 管家在進場時準備好「捕捉 ValueError」
    # 如果順利噴錯並被攔截 ➔ PASS；如果沒噴錯或噴別的錯 ➔ FAIL
    with pytest.raises(ValueError):
        convert(time)
=============================================================================
"""