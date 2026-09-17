def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not Length_Judgment(s):
        return False
    if not Judgment_First_Two(s):
        return False
    if not Only_Num_Eng(s):
        return False
    if not Number_At_The_End(s):
        return False
    return True

def Judgment_First_Two(s):
    if s[:2].isalpha() == True:
        return True
    else:
        return False 

def Length_Judgment(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def Number_At_The_End(s):
    # 【規則 1】如果車牌完全沒有數字、全部都是英文字母，直接視為合法
    if s.isalpha() == True:
        return True

    # 【規則 2】開始尋找第一個出現的數字，用 enumerate 同時取得索引（i）與字元（char）
    for i, char in enumerate(s):
        # 檢查當前字元是不是數字
        if char.isdigit():
            # 檢查規定：第一個出現的數字絕對不能是 '0'（例如 CS05 不合法）
            if char == "0":
                return False
            # 只要找到了第一個數字，就立刻跳出迴圈，因為我們已經鎖定它的位置（i）了
            break

    # 【規則 3】從「第一個數字出現的位置（i）」開始切片到結尾，檢查這段後面是不是全部都是數字
    # 如果全都是數字（代表沒有字母混在數字中間或後面），則回傳 True
    if s[i:].isdigit():
        return True
    # 如果後面夾雜了字母（例如 CS50P），則 s[i:].isdigit() 會是 False，回傳不合法
    else:
        return False
        
    # 註解備忘區：
    # 1. 最後開始的地方一定要是數字 (透過 isdigit 檢查)
    # 2. 數字結束後，後面不能再出現字母 (透過 s[i:].isdigit() 嚴格把關)
    # 3. 第一個數字的地方不能是 0 (透過 char == "0" 攔截)

def Only_Num_Eng(s):
    if s.isalnum() == True:
        return True
    else:
        return False
    

main()