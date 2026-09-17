"""
============================================================
【Python 實戰演進筆記】從過程式寫法到物件導向 (OOP)
============================================================
"""

# ============================================================
# 版本一：基礎過程式寫法 (Procedural)
# 痛點：資料是散落的變數，缺乏整體的「概念」與封裝。
# ============================================================
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()


# ============================================================
# 版本二：使用 Tuple / List / Dict 封裝資料
# 痛點：
# - 用 Tuple (元組) 沒辦法修改資料 (Immutable)。
# - 用 List (列表) 必須記住索引編號 (如 student[0])，容易混淆。
# - 用 Dict (字典) 雖然有鍵值，但寫起來很冗長 (`student["name"]`)。
# ============================================================
def main():
    student = get_student()
    # 如果不小心打錯字或改資料會很不直覺
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()


# ============================================================
# 版本三：初探 Class（自定義數據類型）
# 優點：開始有了物件的概念，可以透過點號 `.` 訪問屬性。
# 痛點：還沒有學會用建構式初始化，屬性必須在外面手動賦值。
# ============================================================
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()


# ============================================================
# 版本四：完整的物件導向 OOP 寫法（使用 __init__ 建構式）
# 優點：
# - 完美封裝！透過 `Student(name, house)` 一行程式碼就建立好物件。
# - 具備可讀性與擴充性，是大型專案的標準寫法。
# ============================================================
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student() -> Student:
    name = input("Name: ")
    house = input("House: ")
    # 呼叫類別名稱（實例化），把資料直接打包進對象裡
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()



"""
============================================================
【Python 實戰演進】類別的建構、防禦性驗證與字串化
============================================================
"""

# ============================================================
# 版本一：使用 __init__ 接收參數並初始化屬性
# ============================================================
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# ============================================================
# 版本二：加入主動拋出例外（raise ValueError）的資料驗證
# 優勢：在物件誕生之前就把關，確保資料絕對正確。
# ============================================================
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# ============================================================
# 版本三：加入 __str__ 方法，讓物件具備自我印出的能力
# 優勢：當呼叫 print(student) 時，會自動執行 __str__ 回傳美觀的字串。
# ============================================================
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    # 直接 print 物件，Python 會自動去尋找並執行類別裡的 __str__ 方法！
    print(student)


def get_student() -> Student:
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()




"""
============================================================
【Python 實戰演進】__str__ 顯示優化與實例方法 (Methods)
============================================================
"""

# ============================================================
# 版本一：使用 __str__ 取代難懂的記憶體地址
# ============================================================
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)  # 直接 print(student) 就會自動觸發 __str__

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# ============================================================
# 版本二：擴充屬性並加入自定義實例方法 (charm)
# 優勢：物件不只存資料，還擁有自己的行為與邏輯。
# ============================================================
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        # 根據當前對象的 patronus 屬性進行邏輯判斷
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🧙"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())  # 呼叫類別內部的實例方法

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()


# ============================================================
# 版本三：精簡回歸基本屬性，探討物件屬性的可變性
# ============================================================
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    # 類別的物件屬性預設是可變的，甚至可以在外部被直接賦值修改
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student() -> Student:
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()



"""
============================================================
【Python 實戰演進】使用 @property 與 Setter 實現嚴格資料驗證
============================================================
"""

class Student:
    def __init__(self, name, house):
        # 注意：這裡刻意不寫底線，直接呼叫 self.name 和 self.house
        # 這樣當物件初始化時，就會自動觸發底下寫好的 Setter 進行嚴格檢查！
        self.name = name
        self.house = house
    
    def __str__(self):
        # 【Getter 觸發時機】：
        # 當這裡嘗試讀取 self.name 與 self.house 時，
        # 就會自動呼叫下方的 @property (Getter) 來取得資料並回傳。
        return f"{self.name} from {self.house}"

    # --------------------------------------------------------
    # name 屬性封裝 (Getter & Setter)
    # --------------------------------------------------------
    @property
    def name(self):
        """Getter：當外部讀取 student.name 時觸發，負責安全回傳內部資料。"""
        # 為什麼變數要多一個底線（self._name）？
        # 1. 區隔：對外的介面叫 name（屬性名稱），對內實際裝資料的變數叫 _name。
        # 2. 防護：如果內部也叫 self.name = name，在 setter 裡賦值時會再次觸發 setter，
        #    導致無限遞迴（Recursion Error）當機！因此需要用 _name 來真正存放資料。
        return self._name

    @name.setter
    def name(self, name):
        """Setter：當外部賦值 student.name = ... 時觸發，負責攔截並檢查資料。"""
        if not name:
            raise ValueError("Missing name")
        # 將驗證過後的乾淨資料存入帶有底線的內部變數中
        self._name = name

    # --------------------------------------------------------
    # house 屬性封裝 (Getter & Setter)
    # --------------------------------------------------------
    @property
    def house(self):
        """Getter：負責安全回傳內部的 _house 資料。"""
        return self._house

    @house.setter
    def house(self, house):
        """Setter：負責在賦值時攔截並檢查 house 是否合法。"""
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        # 同樣存入帶有底線的內部私有變數
        self._house = house


def main():
    try:
        student = get_student()
        print(student)
        
        # 測試防禦機制：嘗試非法修改（會被 Setter 攔截並拋出 ValueError）
        # student.house = "Number Four, Privet Drive"
        
    except ValueError as e:
        print(f"錯誤：{e}")


def get_student() -> Student:
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()




"""
============================================================
【Python 實戰演進】類方法、類變數與 Student.get() 封裝
============================================================
"""

# ============================================================
# 版本一：分院帽 (Hat) - 使用類變數與 @classmethod
# 優勢：不需要實例化多個分院帽物件，直接由類別本身提供共用功能與資料。
# ============================================================
import random

class Hat:
    # 類變數：全體物件/類別共用的常數列表
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        # 使用 cls 訪問類變數，不需要 self
        house = random.choice(cls.houses)
        print(name, "is in", house)

# 直接透過類別名稱呼叫，不需要寫 hat = Hat()
Hat.sort("Harry")


# ============================================================
# 版本二：學生 (Student) - 將物件建立邏輯封裝為類方法 (Factory)
# 優勢：把原本散落在外的 get_student 函式收納進類別內，結構更清晰。
# ============================================================
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    # 定義類方法作為「物件工廠」，專門負責輸入與建立學生
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        # cls(name, house) 相當於呼叫 Student(name, house)
        return cls(name, house)


def main():
    # 直接透過類別呼叫類方法來取得物件，程式碼變得非常直覺！
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

 

"""
============================================================
【Python 實戰演進】巫師、學生與教授的類別繼承設計
============================================================
"""

# ============================================================
# 版本一：各自獨立的類別（存在重複的 name 驗證邏輯）
# ============================================================
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject


# ============================================================
# 版本二：使用繼承（Inheritance）與 super() 消除冗餘程式碼
# 優勢：共用的錯誤檢查與屬性賦值交給父類別 Wizard 處理，子類別更精簡！
# ============================================================
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        # 使用 super() 呼叫父類別 Wizard 的 __init__ 來處理 name 與驗證
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        # 同樣呼叫父類別的初始化，專心處理教授特有的 subject
        super().__init__(name)
        self.subject = subject


def main():
    # 測試建立各種角色物件
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")
    
    print(f"Wizard: {wizard.name}")
    print(f"Student: {student.name} from {student.house}")
    print(f"Professor: {professor.name} teaches {professor.subject}")


if __name__ == "__main__":
    main()



"""
============================================================
【Python 實戰演進】銀行金庫 Vault 與運算子多載
============================================================
"""

# ============================================================
# 版本一：使用傳統方式手動取出屬性相加並創建新物件
# ============================================================
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

def main():
    potter = Vault(100, 50, 25)
    weasley = Vault(25, 50, 100)

    # 手動提取左右兩邊的屬性進行加法運算
    galleons = potter.galleons + weasley.galleons
    sickles = potter.sickles + weasley.sickles
    knuts = potter.knuts + weasley.knuts

    total = Vault(galleons, sickles, knuts)
    print(total)

if __name__ == "__main__":
    main()


# ============================================================
# 版本二：實作 __add__ 達成運算子多載，讓 potter + weasley 直接生效！
# 優勢：程式碼變得極具直覺與物件導向的封裝美感。
# ============================================================
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    # 重載加號運算子 (+)
    def __add__(self, other):
        # self 是左邊的物件 (potter)，other 是右邊的物件 (weasley)
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        
        # 回傳一個全新的 Vault 物件
        return Vault(galleons, sickles, knuts)


def main():
    potter = Vault(100, 50, 25)
    print(f"Potter: {potter}")

    weasley = Vault(25, 50, 100)
    print(f"Weasley: {weasley}")

    # 直接使用 + 運算子將兩個金庫相加，底層會自動呼叫 __add__！
    total = potter + weasley
    print(f"Total: {total}")


if __name__ == "__main__":
    main()



"""
============================================================
【Python 實戰演進】靜態方法 (@staticmethod) 範例
============================================================
"""

class Calculator:
    def __init__(self, owner):
        self.owner = owner

    # 實例方法：需要用到 self (特定的 owner)
    # rust_owner_info(self):
    #     return f"This calculator belongs to {self.owner}"

    # 靜態方法：不需要 self 也不需要 cls，只負責單純的計算邏輯工具
    @staticmethod
    def add(a, b):
        return a + b


def main():
    # 1. 靜態方法可以直接透過「類別名稱」調用，不需要實例化！
    result = Calculator.add(10, 20)
    print(f"10 + 20 = {result}")  # 輸出 30

    # 2. 也可以透過物件調用，但通常習慣直接用類別調用
    calc = Calculator("Harry")
    print(calc.add(5, 5))         # 輸出 10


if __name__ == "__main__":
    main()

"""
============================================================
【Python 複習筆記】從資料結構到物件導向 (OOP) 的演進
============================================================

1. 從多個返回值到容器型別的選擇
   - Tuple (元組, 語法: `(name, house)` 或 `name, house`)
     * 特性：不可變 (Immutable)。一旦建立就不能修改內容（嘗試修改會引發 TypeError）。
     * 時機：當你明確知道資料不該被竄改、只是想安全地打包回傳多個值時使用。
   - List (列表, 語法: `[name, house]`)
     * 特性：可變 (Mutable)。可以隨時修改裡面的元素（例如修正學生的學院）。
     * 缺點：依賴數字索引 (如 `student[0]`)，容易忘記哪個索引代表什麼。
   - Dictionary (字典, 語法: `{"name": name, "house": house}`)
     * 特性：可變、使用具名鍵 (Keys) 存取 (如 `student["name"]`)。
     * 優點：比索引直覺，不需要死記數字代表的含義。

2. 物件導向程式設計 (OOP) 與類別 (Classes)
   - 為什麼需要 Class？
     * 如果一直用通用型別（字典、列表），程式碼會變得繁瑣且缺乏規範。
     * Class（類別）就像是「藍圖」或「模具」，讓你可以自定義屬於自己的資料類型。
   - 核心名詞定義：
     * Class (類別)：自定義數據類型的「藍圖」（首字母通常大寫，例如 `class Student:`）。
     * Object / Instance (對象 / 實例)：用藍圖實際建造出來的「實體」（例如 `student = Student()`）。
     * Attributes (屬性 / 實例變數)：對象內部擁有的變數（例如 `student.name`、`student.house`）。

3. 語法小重點
   - 點號 `.`：用來訪問物件內部的屬性或方法（與模組調用類似）。
   - 防禦性編程習慣：檔案底部保留 `if __name__ == "__main__": main()`，確保該檔案作為模組被引用時不會誤觸發執行。
============================================================
"""



"""
============================================================
【Python 複習筆記】類別的初始化、資料驗證與特殊方法
============================================================

1. 實例方法：`__init__` 與建構式調用
   - 當你寫出 `student = Student(name, house)` 時，Python 會自動呼叫類別內部的 `__init__` 方法。
   - `self` 的意義：
     * `self` 代表的是「剛剛在記憶體中建立好的那個當前對象（實例本身）」。
     * Python 會隱式地把對象傳進 `self`，讓你可以透過 `self.name = name` 把資料綁定到這個對象身上。

2. 用類別進行強大的資料驗證與例外處理 (`raise`)
   - 為什麼要把驗證寫在類別（`__init__`）裡面？
     * 相比於字典或一般變數不管塞什麼都能接受，類別可以把「資料正確性」的邏輯封裝在內部。
     * 如果使用者亂填（例如沒填名字、或是學院打錯），可以主動拋出例外：`raise ValueError("錯誤訊息")`。
   - 優勢：
     * 不會讓錯誤的、殘缺的髒資料污染程式。
     * 可以由外部的 `try...except` 妥善捕捉並處理，而不需要粗暴地用 `sys.exit()` 砍掉整個程式。

3. 物件的字串表達式：`__str__` 方法
   - 當你直接把一個物件丟進 `print(student)` 時，Python 預設只會印出類似 `<__main__.Student object at 0x...>` 的記憶體地址。
   - 解決辦法：
     * 在類別內部定義 `__str__(self)` 方法，回傳一段格式化的字串（例如 `return f"{self.name} from {self.house}"`）。
     * 只要定義了這個方法，當你對該物件呼叫 `print()` 或把它轉換成字串時，Python 就會自動執行它！
============================================================
"""



"""
============================================================
【Python 複習筆記】魔術方法 `__str__` 與自定義實例方法
============================================================

1. 善用 `__str__` 讓物件具備「自我介紹」能力
   - 當直接呼叫 `print(student)` 時，如果沒有定義 `__str__`，Python 預設會印出記憶體地址（例如 `<__main__.Student object at 0x...>`）。
   - 只要在類別中實作 `def __str__(self):`，就能自定義當物件轉為字串時要呈現的內容（通常是給使用者看的友善資訊）。

2. 自定義實例方法 (Methods)
   - 類別不僅能儲存資料（屬性 / 實例變數），還能封裝行為（函數）。
   - 所有在類別中定義的方法，**第一個參數都必須是 `self`**（代表當前對象本身），透過 `self` 可以自由存取該物件內部的屬性（例如 `self.patronus`）。
   - 範例中的 `charm(self)` 方法，能根據學生的守護神動態回傳對應的表情符號，完美展現了物件導向「資料與行為封裝」的核心優勢！
============================================================
"""



"""
============================================================
【Python 複習筆記】屬性 (Properties)、getter、setter 與封裝
============================================================

1. 為什麼需要 @property 與 Setter？
   - 痛點：直接使用 `student.house = "..."` 賦值時，會繞過 `__init__` 裡的驗證，導致任何人都能隨意修改、破壞資料。
   - 解決辦法：透過 **Property** 把屬性保護起來。
     * **Getter (`@property`)**：負責安全地「讀取」資料。
     * **Setter (`@property.setter`)**：負責在資料被「賦值」時進行邏輯檢核（例如檢查是不是四大學院、名字有沒有填）。
   - 神奇之處：當你在程式裡寫下 `student.house = "Gryffindor"` 時，Python 會**自動攔截**並呼叫 Setter 函數，而不是直接覆蓋變數！

2. 變數名稱與底線 (`_`) 的秘密
   - 為什麼要在內部變數加底線（例如 `self._house`）？
     * 如果函式叫 `house`，變數也叫 `house`，名稱會互相衝突。
     * 因此慣例上會把真正的底層儲存變數命名為 `_house`（帶底線），而對外公開的介面則叫 `house`（不帶底線）。
   - 巧妙的初始化：
     * 在 `__init__` 裡面寫 `self.house = house`（不加底線），這樣即使在物件剛建立時，也會自動觸發 Setter 去做防禦性檢查！

3. Python 的核心哲學：「君子協定」
   - 與 Java 或 C++ 等嚴格語言不同，Python **沒有真正的強制私有變數 (Private Variables)**。
   - 帶有底線的變數（如 `_house`）只是一種「君子協定」，意思是：*「我知道技術上可以直接改它，但基於規範我選擇不這樣做」*。如果有人故意去改 `student._house`，Python 還是會讓他過，後果需自行負責！
============================================================
"""



"""
============================================================
【Python 複習筆記】類方法、類變數與工廠設計模式
============================================================

1. Python 萬物皆類別 (Classes)
   - 像 `int`、`str`、`list`、`dict` 這些內建型別，本質上全部都是類別。
   - 當你寫 `str.lower()` 或 `list.append()` 時，其實就是在對該類別的實例（對象）呼叫內建方法。
   - 慣例提醒：內建類別全小寫（如 `int`），而我們自定義的類別則採用首字母大寫（如 `Student`）。

2. 類變數 (Class Variables) 與 類方法 (Class Methods)
   - 為什麼需要 `@classmethod`？
     * 當某些功能或資料不需要綁定在特定的「單一物件（`self`）」上時（例如全世界只需要一頂分院帽、或者純粹當作資料與功能的命名空間容器），就不需要寫 `__init__` 去實例化。
   - 參數的轉變：
     * 實例方法使用 `self`（指向具體某個實例）。
     * 類方法使用 `@classmethod` 裝飾器，且第一個參數按照慣例改為 **`cls`**（代表類別本身）。

3. 用類方法實作「工廠方法」 (Factory Method)
   - 痛點：原本獲取使用者輸入並建立物件的 `get_student()` 獨立放在外面，會導致學生相關的邏輯四處散落。
   - 解決辦法：把輸入與建立對象的邏輯寫進類別內部的 `get(cls)` 方法中。
   - 巧妙之處：
     * 因為是類方法，所以我們**不需要先建立學生**就能呼叫它。
     * 直接在方法內回傳 `cls(name, house)`，這等同於呼叫 `Student(name, house)`，完美實現了將「物件建立邏輯」封裝在類別內部的物件導向設計！
============================================================
"""



"""
============================================================
【Python 複習筆記】類別繼承 (Inheritance) 與例外階層
============================================================

1. 為什麼需要「繼承 (Inheritance)」？
   - 痛點：當多個類別（如 `Student` 與 `Professor`）都有重複的屬性或錯誤檢查邏輯（例如都有 `name` 檢查），如果各自寫一份就會造成程式碼冗餘（Duplicate Code）。
   - 解決辦法：抽象出一個共同的父類別（如 `Wizard`），把共用的屬性與驗證邏輯集中管理，讓子類別去「繼承」它。

2. 如何使用繼承與 `super()`？
   - 語法：在定義子類別時，於括號內填入父類別名稱，例如 `class Student(Wizard):`。
   - 透過 `super().__init__(name)`：
     * 指向並呼叫「父類別」的初始化方法，將子類別收到的共用參數（如 `name`）傳給父類別去處理，避免重複寫驗證程式碼。
     * 之後子類別只需專心處理自己獨有的屬性（例如學生的 `house`、教授的 `subject`）。

3. Python 的例外階層 (Exception Hierarchy)
   - Python 的內建例外（如 `ValueError`、`KeyError` 等）本身也是透過繼承體系組織起來的。
   - 好處：當你在寫 `except` 時，若不只想捕捉特定的錯誤，也可以捕捉其父類別（甚至是更上層的 `Exception`），這使得例外處理具有極高的靈活性與擴充性！
============================================================
"""



"""
============================================================
【Python 複習筆記】運算子多載 (Operator Overloading)
============================================================

1. 什麼是運算子多載？
   - 運算子（如 `+`、`-`、`==`）在 Python 中不一定只能做數學加法或字串拼接。
   - 透過實作特定的魔術方法（例如 `__add__`），我們可以教 Python 讓自定義的物件（如金庫 `Vault`）也能直接相加。

2. `__add__(self, other)` 的運作原理
   - 當你在程式中寫下 `total = potter + weasley` 時：
     * **`self`**：代表加號「左邊」的對象（即 `potter`）。
     * **`other`**：代表加號「右邊」的對象（即 `weasley`）。
   - 過程：Python 會自動攔截這個加法運算，呼叫左側物件的 `__add__` 方法，並把右側物件作為 `other` 傳進去。
   - 返回值：我們可以在方法內部將兩者的資產相加，並透過 `return Vault(...)` 建立並回傳一個全新的物件。

3. 其他常見的可重載運算子（Magic Methods）
   - 算術運算：`__sub__` (-), `__mul__` (*)
   - 比較運算：`__eq__` (==), `__lt__` (<), `__gt__` (>)
   - 原地賦值：`__iadd__` (+=)
   - 注意：Python 無法讓你自創全新的運算符號（例如表情符號），但內建的豐富清單已經足夠應付絕大多數的設計需求！
============================================================
"""



"""
============================================================
【Python 複習筆記】靜態方法、例外階層與運算符重載魔術方法
============================================================

1. 什麼是靜態方法 (`@staticmethod`)？它是幹嘛的？
   - 定義：靜態方法是不需要接收 `self`（實例本身）也不需要接收 `cls`（類別本身）的普通函數。
   - 特點：它只是剛好「邏輯上跟這個類別相關」，所以被放在類別的肚子裡管理。它**不能**訪問或修改類別或實例的任何屬性。
   - 為什麼要用它？
     * 當你有一些工具性質的函數，它完全獨立於物件狀態，但你希望把它們收納在類別裡面（避免汙染全域命名空間）時，就會使用 `@staticmethod`。
     * 對比：
       - 實例方法：需要 `self`（跟特定物件綁定）。
       - 類別方法 (`@classmethod`)：需要 `cls`（跟整個類別共用資料互動）。
       - 靜態方法 (`@staticmethod`)：誰都不需要，就是一個純粹住在類別裡面的獨立函數。

2. Python 的內建例外階層 (Exception Hierarchy)
   - Python 的所有錯誤（Exception）都是透過樹狀階層組織的（例如 `ValueError` 繼承自 `Exception`，而 `Exception` 繼承自 `BaseException`）。
   - 好處：在用 `try...except` 時，你可以捕捉具體的錯誤（如 `ZeroDivisionError`），也可以直接捕捉其上層的父類別來統一處理一類錯誤。

3. 物件導向的高級玩法：運算符重載魔術方法 (Operator Overloading)
   - 透過實作這些雙下劃線開頭的魔術方法，你可以讓自己定義的類別（物件）支援像內建數字一樣的加減乘除或比較運算：
     * 一元運算符：`__pos__ (+)`、`__neg__ (-)`、`__abs__ (abs())`
     * 二元算術運算：`__add__ (+)`、`__sub__ (-)`、`__mul__ (*)`、`__truediv__ (/)`
     * 原地賦值運算：`__iadd__ (+=)`、`__isub__ (-=)` 等
     * 比較運算：`__eq__ (==)`、`__lt__ (<)`、`__gt__ (>)` 等
     * 位元運算：`__and__ (&)`、`__or__ (|)` 等
============================================================
"""



"""
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning

很長但明確的列表，裡面是所有可重載的運算符
一元運算符（Unary Operators）
__pos__(self)：正號 +
__neg__(self)：負號 -
__abs__(self)：絕對值 abs()
__invert__(self)：按位取反 ~

二元算術運算符（Binary Arithmetic Operators）
__add__(self, other)：加法 +
__sub__(self, other)：減法 -
__mul__(self, other)：乘法 *
__truediv__(self, other)：除法 /
__floordiv__(self, other)：整除 //
__mod__(self, other)：取模 %
__pow__(self, other[, modulo])：冪運算 **

反向算術運算符（Reflected Arithmetic Operators）
當左側運算子不支援該操作時調用（例如 2 + obj）：__radd__、__rsub__、__rmul__、__rtruediv__ 等。

賦值運算符（In-place / Augmented Assignment）
__iadd__(self, other)：原地加法 +=
__isub__(self, other)：原地減法 -=
__imul__(self, other)：原地乘法 *=
__itruediv__(self, other)：原地除法 /=

比較運算符（Comparison Operators）
__eq__(self, other)：等於 ==
__ne__(self, other)：不等於 !=
__lt__(self, other)：小於 <
__le__(self, other)：小於等於 <=
__gt__(self, other)：大於 >
__ge__(self, other)：大於等於 >=

位元運算符（Bitwise Operators）
__lshift__(self, other)：左移 <<
__rshift__(self, other)：右移 >>
__and__(self, other)：按位與 &
__xor__(self, other)：按位異或 ^
__or__(self, other)：按位或 |

"""

