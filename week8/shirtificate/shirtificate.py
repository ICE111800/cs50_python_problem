from pathlib import Path
from fpdf import FPDF

# --- 常數定義 (Constants) ---
PAGE_WIDTH_MM: float = 210.0
SHIRT_WIDTH_MM: float = 150.0
SHIRT_Y_POS: float = 50.0
NAME_Y_POS: float = 100.0
BACKGROUND_IMAGE: str = "shirtificate.png"
OUTPUT_FILENAME: str = "shirtificate.pdf"


class Cs50_shirt(FPDF):
    """
    A PDF generator class specifically designed to create CS50 Shirtificates.

    Inherits from fpdf.FPDF to handle A4 page setup, image positioning,
    and text rendering dynamically.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the PDF settings (A4 portrait) and execute the rendering pipeline.

        :param name: The name of the user to be printed on the shirt
        :type name: str
        :raise ValueError: If the provided name is empty or contains only whitespace.
        :raise FileNotFoundError: If the required 'shirtificate.png' background image is missing.

        """
       
        super().__init__(orientation="P", unit="mm", format="A4")

        # 防禦性編程：檢查名字是否為空或只有空白字元
        if not name or not name.strip():
            raise ValueError("名字不能為空!")
        
        self.name: str = name.strip()

        # 防禦性編程：檢查圖片檔案是否存在，避免程式因找不到圖而崩潰
        image_path = Path(BACKGROUND_IMAGE)
        if not image_path.is_file():
            raise FileNotFoundError("找不到背景圖片: 'shirtificate.png'")

        # 自動化執行建構流程
        self.add_page()
        self.picture()
        self.text()

    def picture(self) -> None:
        """
        Calculate coordinates and place the T-shirt background image centered on the page.
        
        :return: None
        :rtype: None
        """
        # A4 寬度為 210mm，圖片寬度設定為 150mm
        x_coord: float = (PAGE_WIDTH_MM - SHIRT_WIDTH_MM) / 2
        self.image(BACKGROUND_IMAGE, x=x_coord, y=SHIRT_Y_POS, w=SHIRT_WIDTH_MM)


    def text(self) -> None:
        """
        Render the top title and overlay the user's name onto the T-shirt.
        
        :return: None
        :rtype: None
        """
        # 繪製頂端標題（黑色字體）
        self.set_font("helvetica", style="B", size=16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 20, "CS50 Shirtificate", align="C")

        # 繪製疊在 T 恤上的使用者名字（白色字體）
        self.set_font("helvetica", style="B", size=24)
        self.set_text_color(255, 255, 255)
        self.set_y(NAME_Y_POS) # 移動到 T 恤胸口的高度
        self.cell(0, 10, self.name, align="C")
        

def main() -> None:
    """
    Main entry point of the script.

    Prompts the user for their name, instantiates the Cs50_shirt class,
    and outputs the resulting PDF file.
    
    :return: None
    :rtype: None
    """
    try:
        name = input("Name: ")
        pdf = Cs50_shirt(name)
        pdf.output(OUTPUT_FILENAME)
        print(f"成功產生 {OUTPUT_FILENAME}！")
    except (ValueError, FileNotFoundError) as e:
        print(f"發生錯誤:{e}")


if __name__ == "__main__":
    main()