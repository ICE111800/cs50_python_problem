import csv
import sys
import os

def main() -> None:
    # 1. 取得命令列參數（讀取檔名與寫入檔名)
    read_file, write_file = determine_command_line_arguments()
    # 2. 執行 CSV 讀取、資料清洗與寫入流程
    result = read_and_write_csv(read_file, write_file)

    print("Copy successful")
    
def determine_command_line_arguments() -> tuple[str, str]:
    """檢查命令列參數的數量與副檔名是否合規"""
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    read_file_name = sys.argv[1]
    write_file_name = sys.argv[2]

    # 確保兩者都是 .csv 檔案
    if not read_file_name.endswith(".csv") or not write_file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    return read_file_name, write_file_name

def read_and_write_csv(read_file: str, write_file: str) -> None:
    """防禦性讀取舊 CSV、拆解整理名字，並寫入新 CSV"""
    old_file_list = []

    # 防禦性讀取檔案：使用 try...except 避免檔案不存在時程式崩潰
    try:
        with open(read_file, encoding="utf-8") as old_file:
            # 使用 DictReader 讓每一行自動變成字典格式（以表頭為 Key）
            reader = csv.DictReader(old_file)
            for row in reader:
                # 確保 row 裡面有 name 欄位且格式正確包含逗號
                if "name" in row and "," in row["name"]:
                    # 將 "Last, First" 透過逗號與空格切開（限制切 1 次）
                    last, first = row["name"].split(", ", 1)

                    # 將整理好的資料包成字典，放入清單中
                    old_file_list.append({
                        "first": first.strip(),
                        "last": last.strip(),
                        "house":row.get("house", "").strip()
                    })
                else:
                    sys.exit(f"Malformed row in CSV: {row}")

    except FileNotFoundError:
        sys.exit(f"Could not read {read_file}")

    # 寫入新檔案
    try:
        with open(write_file, "w", newline="", encoding="utf-8") as new_file:
            # 宣告 DictWriter 並指定新檔案的欄位順序
            writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])

            # 寫入標題列 (Header)
            writer.writeheader()

            # 逐行寫入整理好的學生字典資料
            for row in old_file_list:
                writer.writerow(row)
    except OSError:
        sys.exit(f"Could not write to {write_file}")

if __name__ == "__main__":
    main()