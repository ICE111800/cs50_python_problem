import sys
import inflect

def main():
    # 初始化 inflect 引擎，用來處理英文單字複數與串接格式
    p = inflect.engine()

    # 宣告一個空清單，用來依序儲存使用者輸入的名字
    names = []

    # 使用 while True 建立無限迴圈，持續收集使用者輸入
    while True:
        try:
            # 取得輸入並去除前後空白
            name_input = input("Name: ").strip()

            # 【防禦性編寫】：如果使用者沒打字直接按 Enter，略過這次迴圈，避免空字串被塞進清單
            if not name_input:
                continue

        # 攔截使用者的 Ctrl + D (EOFError)，當使用者結束輸入時跳出迴圈
        except EOFError:
            print()
            break

        # 將合法輸入的名字加入清單中
        names.append(name_input)

    # 【防禦性防護】：如果使用者什麼名字符都沒有輸入就直接按 Ctrl+D，安全退出程式
    if not names:
        sys.exit()

    # 輸出結果：
    # 這裡直接將 names 清單交給 p.join() 處理並印出，
    # 刻意不將 names 重新賦值（Reassignment）改寫成字串，
    # 確保 names 維持「清單」型態，避免在大型專案中引發型態錯亂或覆蓋的潛在 Bug。
    print(f"Adieu, adieu, to {p.join(names)}")

if __name__ =="__main__":
    main()
    

    

