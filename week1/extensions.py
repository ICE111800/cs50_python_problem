def main():
    file = input("File name: ").strip().lower()
    print(Change_Media_Type(file))

def Change_Media_Type(file):
    match file:
        case _ if file.endswith(".gif"):
            return "image/gif"
        case _ if file.endswith(".jpg"):
            return "image/jpeg"
        case _ if file.endswith(".jpeg"):
            return "image/jpeg"
        case _ if file.endswith(".png"):
            return "image/png"
        case _ if file.endswith(".pdf"):
            return "application/pdf"
        case _ if file.endswith(".txt"):
            return "text/plain"
        case _ if file.endswith(".zip"):
            return "application/zip"
        case _ if file.endswith(""):
            return "application/octet-stream"
        case _:
            return "application/octet-stream"
    
if __name__ == "__main__":
    main()


# def main():
#     while True:
#         file = input("File name: ").strip().lower().rsplit(".", 1)
        
#         # 1. 處理沒有副檔名的邊際情況（例如輸入 "cat"）
#         # 當找不到點時，rsplit 會回傳長度為 1 的列表，這時我們手動塞一個空字串或預設副檔名進去
#         if len(file) == 1:
#             file.append("") 
            
#         print(Change_Media_Type(file))
#         break

# def Change_Media_Type(file):
#     # file[0] 是檔名主體，file[1] 是副檔名
#     ext = file[1]
    
#     # 2. 因為前綴不固定（有 image/, application/, text/），
#     # 這裡必須在函式內部另外用條件判斷去手動組合
#     if ext == "gif":
#         return "image/gif"
#     elif ext in ["jpg", "jpeg"]:
#         return "image/jpeg"
#     elif ext == "png":
#         return "image/png"
#     elif ext == "pdf":
#         return "application/pdf"
#     elif ext == "txt":
#         return "text/plain"
#     elif ext == "zip":
#         return "application/zip"
#     else:
#         return "application/octet-stream"

# if __name__ == "__main__":
#     main()



