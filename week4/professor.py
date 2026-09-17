from random import randint
import sys

def main():
    get_point = 0
    error_times = 3
    total_tests = 0

    # 取得遊戲難度等級 (1, 2, 3)
    level = get_level()

    # 總共進行 10 次數學測驗
    while total_tests < 10:
        # 根據等級動態產生兩個隨機數字
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        # 每次題目給予使用者 3 次作答機會
        for _ in range(error_times):
            try:
                user_result = input(f"{x} + {y} = ")
            except EOFError:
                # 攔截 Ctrl + D，優雅退出程式
                sys.exit("\nExiting program.")

            # 【防禦性編寫】：確保使用者輸入的是合法整數
            try:
                user_result = int(user_result)
            except ValueError:
                print("EEE")
                continue # 轉換失敗印出 EEE 並跳過這次嘗試，重新輸入

            # 判斷答案是否正確
            if user_result == result:
                get_point += 1
                break # 答對了，跳出 3 次機會的迴圈
            else:
                print("EEE")
        else:
            # 【Python 獨家技巧 (for...else)】：
            # 如果 for 迴圈完整跑完 3 次都沒有被 break（代表 3 次全猜錯），就會執行這裡印出正確答案
            print(f"{x} + {y} = {result}")

        total_tests += 1

    # 測驗結束，輸出總得分
    print(f"Score: {get_point}")


def get_level():
    # 迴圈確保使用者輸入合法的等級 (1, 2, 3)
    while True:
        try:
            level = input("Level: ").strip()
        except EOFError:
            sys.exit("\nExiting program.")

        try:
            level = int(level)
        except ValueError:
            continue

        # 檢查是否為規定的 1, 2, 3 級別
        if level in [1,2,3]:
            return level

def generate_integer(level):
    # 【進階優化】：使用數學次方動態計算範圍，不再死板地寫死（Hardcode），支援未來擴充位數
    if level not in [1,2,3]: 
        raise ValueError # 依規定，不符合的 level 必須引發 ValueError

    # 1 位數範圍是 0~9；2 位數以上是 10^(level-1) 到 10^level - 1
    start = 0 if level == 1 else 10 ** (level - 1)
    end = (10 ** level) - 1

    return randint(start, end)

if __name__ == "__main__":
    main()