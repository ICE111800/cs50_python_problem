import sys
import os
from PIL import Image, ImageOps

def main() -> None:
    # 執行命令列參數與副檔名的驗證，並取得輸入與輸出檔案路徑
    input_pic, output_pic = validate_args_and_extensions()

    # 讀取圖片、進行調整、貼上 T 恤並存檔
    read_and_save_modified_images(input_pic, output_pic)

def validate_args_and_extensions() -> tuple[str, str]:
    """
    驗證命令列參數的數量是否正確，
    並檢查輸入與輸出檔案的副檔名是否合法且相符。
    """
    # 檢查參數數量是否剛好為 2 個（加上檔名本身共 3 個元素）
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # 取得輸入與輸出檔案的副檔名，並轉成小寫以利後續比對
    input_exts = os.path.splitext(sys.argv[1])[-1].lower()
    output_exts = os.path.splitext(sys.argv[2])[-1].lower()

    # 檢查副檔名是否為允許的格式 (.jpg, .jpeg, .png)
    if input_exts not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")
    elif output_exts not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
    # 檢查輸入與輸出的副檔名是否一致
    elif input_exts != output_exts:
        sys.exit("Input and output have different extensions")

    # 驗證通過，回傳命令列中的檔案路徑
    return sys.argv[1], sys.argv[2]

def read_and_save_modified_images(input_pic: str, output_pic: str) -> None:
    """
    使用 Pillow 開啟圖片、調整尺寸、套用 T 恤圖層，並寫入輸出檔案。
    """
    # 嘗試開啟 T 恤範本圖片
    try:
        # 使用 with 確保離開區塊時自動關閉圖片檔案，釋放資源
        with Image.open("shirt.png") as shirt:
            # 取得 T 恤的寬高，作為目標調整尺寸
            standard_width, standard_height = shirt.size
            target_size = (standard_width, standard_height)

            # 嘗試開啟使用者輸入的照片
            try:
                with Image.open(input_pic) as input_image:
                    # 使用 ImageOps.fit 將輸入照片裁切並縮放到與 T 恤相同的尺寸
                    input_resize_pic = ImageOps.fit(input_image, target_size)

                    # 將 shirt 貼到調整好尺寸的照片上（第二個 shirt 作為透明遮罩）
                    input_resize_pic.paste(shirt, shirt)

                    # 嘗試將合成後的圖片儲存至指定的輸出路徑
                    try:
                        input_resize_pic.save(output_pic)
                    except OSError:
                        sys.exit("File cannot be written")

            except FileNotFoundError:
                sys.exit("Input does not exist")

    except FileNotFoundError:
        sys.exit("shirt.png does not exist")

if __name__ == "__main__":
    main()

