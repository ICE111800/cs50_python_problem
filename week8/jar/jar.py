class Jar:
    def __init__(self, capacity=12):
        """
        【初始化方法（建構子）】
        當你寫 Jar() 或 Jar(10) 時，Python 會自動呼叫這個方法來打造一個新的餅乾罐。
        """
        # 這裡把傳進來的容量指定給 self.capacity。
        # ⚠️ 注意：這裡刻意不用 self._capacity，而是用 self.capacity，
        # 這樣就會「自動觸發底下的 setter」去檢查這個容量有沒有小於 0！
        self.capacity = capacity

        # 一開始剛做好的餅乾罐裡面是空的，所以數量（size）設為 0
        self._size = 0
        
    def __str__(self):
        """
        【字串轉換方法】
        當你使用 print(jar) 或 str(jar) 時，Python 會自動呼叫這個方法。
        它會回傳「目前餅乾數量」個數的 🍪 字串。
        """
        return "🍪" * self._size

    def deposit(self, n):
        """
        【存入餅乾方法】
        把 n 片餅乾放進罐子裡。
        """
        # 檢查：如果「目前餅乾數 + 打算放進去的 n」超過了容量上限
        if (self._size + n) > self.capacity:
            raise ValueError
        # 沒問題的話，把餅乾數量增加 n
        self._size += n

    def withdraw(self, n):
        """
        【取出餅乾方法】
        從罐子裡拿走 n 片餅乾。
        """
        # 檢查：如果目前罐子裡的餅乾比你想拿的還要少
        if self._size < n:
            raise ValueError
        # 沒問題的話，把餅乾數量減少 n
        self._size -= n

    @property
    def capacity(self):
        """
        【Getter：容量屬性】
        扮演「守衛」或「唯讀窗口」的角色。
        當外部有人想查看餅乾罐容量（例如 print(jar.capacity)）時，Python 會叫醒這個方法。
        """
        # 它負責把藏在暗處的真實變數 _capacity 回報給外面的人
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        【Setter：容量設定器】
        扮演「安檢人員」的角色。
        每當有人「設定」或「修改」容量時（例如剛建立 Jar(12) 的那一刻，或是未來有人想改容量），
        Python 會自動把新數字傳進這個方法進行審查。
        """
        # 審查規則：如果容量小於 0（負數）
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        
        # 審查通過！把合法的容量存進真正的倉庫變數 _capacity 裡面
        self._capacity = capacity

    @property
    def size(self):
        """
        【Getter：數量屬性】
        當外部想知道裡面有幾片餅乾時（例如 print(jar.size)），呼叫這個方法。
        注意：size 沒有寫 setter，代表它是「唯讀」的，別人不能直接竄改 size，
        只能透過 deposit 或 withdraw 來改變它。
        """
        return self._size


def main():
    # 創建一個預設容量為 12 的餅乾罐物件
    jar = Jar(12)
    print(f"初始容量: {jar.capacity}")
    print(f"罐子裡的餅乾: {jar}")       # 會自動觸發 __str__

    # 存入幾片餅乾
    jar.deposit(3)
    print(f"存入 3 片後: {jar}")
    print(f"目前的 size: {jar.size}")   # 呼叫 size 屬性（不用加 ()）

    # 再存入幾片
    jar.deposit(5)
    print(f"再存入 5 片後: {jar}")
    print(f"目前的 size: {jar.size}")

    # 拿走餅乾
    jar.withdraw(2)
    print(f"拿走 2 片後: {jar}")
    print(f"目前的 size: {jar.size}")

    # 試看看超過容量會怎樣（會引發 ValueError）
    try:
        jar.deposit(20)
    except ValueError:
        print("哎呀！超過容量了，無法放入！")


if __name__ == "__main__":
    main()



# =============================================================================
# 【Python 物件導向 (OOP) 與 Cookie Jar 觀念總複習筆記】
# =============================================================================
"""
一、 類別 (Class) 與 物件 (Instance) 的區別
-----------------------------------------------------------------------------
* Jar (大寫)   : 這是「藍圖」（類別名稱），本身不能用，是用來創造東西的工廠。
* jar (小寫)   : 這是用藍圖實際做出來的「具體物件」。我們對外操作、呼叫方法、
                 存取屬性，全部都是對著你手上那台具體物件發號施令。

二、 什麼是 self？
-----------------------------------------------------------------------------
* self 代表「這個物件自己」或「當前正在被操作的那個餅乾罐本人」。
* 當你寫 jar1.deposit(3) 時，Python 會自動把 jar1 當作第一個參數傳進去，
  也就是類別裡面的 self。因此：
  - self.capacity 意思是：「我這個餅乾罐的容量」。
  - self._size 意思是：「我這個餅乾罐裡面目前的餅乾數」。

三、 為什麼變數要多一個底線 _？
-----------------------------------------------------------------------------
* 無底線（例如 self.capacity）：對外公開的介面（搭配 @property 與 setter）。
* 有底線（例如 self._capacity）：內部真正用來在記憶體中存放資料的私有變數。
* 黃金法則：
  - 在類別內部存取、修改數值時，為了安全或配合 Getter/Setter，通常會直接
    去讀寫帶底線的變數（例如 self._size）。
  - 對外（給使用者或別的函式），則使用沒有底線的名字（例如 jar.capacity）。
  - 這樣做能有效區隔對外介面與內部儲存，並避免在 setter 裡面直接對自己賦值
    而造成「無限迴圈 (Recursion Error)」當機。

四、 @property (Getter) 與 .setter 的完全解析
-----------------------------------------------------------------------------
1. @property (Getter) —— 唯讀窗口 / 回報員
   * 功能：把一個原本需要加小括號才能執行的函數（例如 jar.size()），包裝成
     可以直接像變數一樣調用的樣子（jar.size，不用加 ()）。
   * 運作時機：當外面的人試圖「讀取」這個屬性時自動觸發。
   * 規則：可以單獨存在（代表該屬性是唯讀的，例如 size）。

2. @屬性名稱.setter (Setter) —— 安檢守衛 / 寫入閘口
   * 功能：專門負責在資料「寫入/修改」時進行攔截與嚴格檢查。
   * 運作時機：當有人試圖「賦值或修改」這個屬性時自動觸發（例如在一開始 
     __init__ 賦值，或是日後修改 jar.capacity = 20）。
   * 規則：
     - 不能單獨存在，必須依附在已經存在的 @property 上面。
     - 名字必須完全一致（@capacity.setter 的名字必須跟上方屬性名一樣）。

五、 屬性 (Attribute) vs 方法 (Method) 的呼叫差異
-----------------------------------------------------------------------------
* 屬性 (Attribute，有 @property 的)：像是容量、大小，不用加小括號。
  範例：print(jar.capacity)、print(jar.size)
* 方法 (Method，像是 deposit、withdraw)：這是動作，呼叫時必須加小括號，
  且要帶入對應的參數。
  範例：jar.deposit(3)、jar.withdraw(1)
"""



# =============================================================================
# 【Python 物件導向深度觀念：屬性、私有變數與內部修改機制】
# =============================================================================
"""
一、 為什麼修改數據（如 deposit/withdraw）要用 self._size，而不是 self.size？
-----------------------------------------------------------------------------
* 由於 size 只有寫 @property（Getter），沒有寫對應的 .setter。
* Python 的鐵律：如果一個屬性只有 Getter 卻沒有 Setter，代表它是「絕對唯讀」的。
* 因此，當你在內部要對數量做增加或扣除時（例如 self._size += n），
  「絕對不能」寫成 self.size += n，否則會當場引發：
  AttributeError: can't set attribute 'size'。
* 結論：內部要改資料時，必須直接去操作真正存放數值的私有倉庫 `self._size`。

二、 「讀取」與「寫入」的觸發時機（安檢機制怎麼運作？）
-----------------------------------------------------------------------------
1. 讀取屬性（例如 print(jar.capacity)、if self.size + n > ...）：
   * 會觸發對應的 @property (Getter)。
   * 它的工作只是「回報數值」，不會進行任何安全檢查。
2. 寫入 / 賦值屬性（例如 jar.capacity = 15，或 __init__ 裡的 self.capacity = capacity）：
   * 會觸發 @capacity.setter 去進行嚴格的安檢（例如檢查是否小於 0）。
   * 如果該屬性「沒有」寫 setter（像 size 一樣），硬要賦值就會直接報錯。
3. 直接碰觸帶底線的變數（例如 self._size += n 或 self._capacity = 15）：
   * 完全不會經過任何 Getter 或 Setter！
   * 就像直接把手伸進倉庫拿東西，安檢門不會被驚動。

三、 總結：什麼時候用 _？什麼時候不用？
-----------------------------------------------------------------------------
* 對外（給外部使用者或別的函式調用）：
  使用沒有底線的名字（例如 jar.capacity、jar.size），透過 @property 確保安全。
* 對內（給類別自己的方法，如 deposit、withdraw 內部邏輯）：
  直接操作帶底線的變數（例如 self._size），因為在自己家裡不需要每次都過安檢門。
"""



# =============================================================================
# 【進階補充：為什麼 `self.size = 0` 能動？這樣寫有什麼隱藏風險？】
# =============================================================================
"""
一、 為什麼在 __init__ 寫 `self.size = 0` 不會馬上報錯？
-----------------------------------------------------------------------------
* Python 是動態語言。當執行到 `self.size = 0` 時，如果物件身上還沒有 
  `size` 這個屬性，Python 就會直接在記憶體中「動態建立」一個名為 `size` 
  的普通實例變數，並把 0 塞進去。
* **它繞過了底下的 `@property`**：因為這是直接賦值建立新變數，所以它
  不會去呼叫底下定義的 `def size(self):`。

二、 這樣寫的隱藏風險（為什麼不建議這樣做？）
-----------------------------------------------------------------------------
1. 破壞了 @property 的封裝意義：
   本來希望 `size` 是個透過 `@property` 唯讀回報數值的窗口，結果在初始化
   時卻直接用 `self.size = 0` 把他變成普通變數，容易讓人混淆。
2. 變數名稱打架與維護災難：
   如果在初始化寫 `self.size = 0`，但在其他方法（如 deposit）裡卻寫了 
   `self._size += n`，會導致記憶體中同時存在 `self.size` 和 `self._size` 
   兩套不同的變數，極容易引發混亂或難以捉摸的 Bug。

三、 最佳實踐（Best Practice）總結
-----------------------------------------------------------------------------
* 內部真正用來存資料、會被頻繁加減修改的變數：
  統一使用帶底線的私有變數（例如 `self._size = 0`）。
* 對外唯讀的窗口：
  使用 `@property def size(self): return self._size`。
* 這樣分工最明確，能確保所有的讀取都走同一套邏輯，程式碼也最安全易讀！
"""



# =============================================================================
# 【核心觀念突破：為什麼 capacity 沒事，但 size 亂寫會「兩套變數打架」？】
# =============================================================================
"""
一、 什麼是「動態建立實例變數」與「繞過 @property」？
-----------------------------------------------------------------------------
* 當你寫 `self.size = 0` 時：
  Python 會在當前這個物件的記憶體中，直接硬生生貼上一個名為 `size` 的普通變數，
  並把 0 塞進去。
* 為什麼會繞過 @property？
  因為 `@property` 是 **Getter（負責讀取）**。Python 的規則是：只有當你在外面
  「讀取」它（如 `print(jar.size)`）時才會叫醒 Getter；當你在初始化進行「寫入/賦值」
  時，它根本不會理會 Getter，而是直接在記憶體造一個新變數。

二、 為什麼 capacity 只有一套資料，不會打架？（完美封裝）
-----------------------------------------------------------------------------
* 因為 capacity 擁有「完整的雙向通道」（同時寫了 Getter 與 Setter）：
  - 讀取時：透過 `@property def capacity` 回報 `self._capacity`。
  - 寫入時：透過 `@capacity.setter` 把新數字統一存進 `self._capacity`。
* **妙就妙在**：無底線的 `self.capacity` 其實**根本沒有在記憶體中獨立存資料**！
  它只是一個對外的代理人，所有真實資料全部集中流向同一個地方（`self._capacity`）。
  所以自始至終都只有一套資料，完全不會打架。

三、 為什麼 size 如果亂寫會出事？（兩套變數互相打架）
-----------------------------------------------------------------------------
* 因為 size 「只有 Getter（唯讀），沒有寫 Setter」：
  - 如果你在 `__init__` 偷懶寫了 `self.size = 0`，因為找不到 setter，Python 就會
    自己動態生出一個獨立的變數叫 `self.size`（值為 0，永遠不動）。
  - 但你在 deposit 裡面卻又是對著 `self._size += n` 做加減！
  - **這就出事了**：記憶體裡同時存在兩個不相幹的東西——一個是初始化的 `self.size`，
    另一個是 deposit 實際加減的 `self._size`。兩套變數同時存在、互相打架，極易出錯。

四、 最終黃金法則
-----------------------------------------------------------------------------
1. 有完整 Getter/Setter 的屬性（如 capacity）：可以透過屬性介面統一收編資料。
2. 唯讀或無 Setter 的屬性（如 size）：初始化與內部加減時，乖乖統一操作帶底線的
   私有變數（例如 `self._size = 0` 與 `self._size += n`），千萬不要亂用無底線賦值！
"""

"""
# 錯誤寫法 原因如下:
class Jar:
    def __init__(self, capacity=12) -> None:
        self.capacity = capacity
        self.size = 0

    def __str__(self) -> str:
        return f"{'🍪'*self.size}"

    def deposit(self, n: int) -> None:
        self.size += n

    def withdraw(self, n: int) -> None:
        self.size -= n

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self,capacity: int) -> None:
        if capacity < 0:
            raise ValueError("Invalid capacity of the jar")
        self._capacity = capacity

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self,size: int) -> None:
        if size < 0:
            raise ValueError("Too few cookies")
        if size > self.capacity:
            raise ValueError("Too many cookies")
        self._size = size
"""
# =============================================================================
# 【架構觀念：為什麼不建議幫 size 寫 Setter？（全套屬性包裝的隱藏陷阱）】
# =============================================================================
"""
一、 陷阱一：初始化順序依賴與隱形炸彈（Initialization Order Trap）
-----------------------------------------------------------------------------
* 如果在 `@size.setter` 裡面去檢查容量（例如 `if size > self.capacity:`），
  會讓 `size` 的賦值動作**強烈依賴**於 `self.capacity` 是否已經先生出來。
* **致命危機**：如果在 `__init__` 中不小心把兩行順序顛倒（先設 `size = 0`，
  後設 `capacity`），當執行到 `size = 0` 觸發 setter 時，Python 會因為還沒讀到 
  `self.capacity` 而當場崩潰報錯 (`AttributeError`)。
* 這會讓程式碼的正確性變得取決於「行數的上下順序」，非常脆弱。

二、 陷阱二：將「行為動作」誤當成「屬性賦值」的效應
-----------------------------------------------------------------------------
* 寫法對比：
  - 正統寫法：餅乾數量是由「行為」改變的（透過 `deposit` / `withdraw` 操作 `self._size`）。
  - 陷阱寫法：允許直接對 `size` 賦值（`self.size += n`）。
* 當你寫 `self.size += n` 時，背後會默默啟動一段超長的連鎖反應：
  1. 呼叫 Getter 讀取目前數字
  2. 進行加法運算
  3. 呼叫 Setter 進行賦值
  4. 在 Setter 內再次執行冗長的防呆檢查（如檢查 capacity）
* 只是想簡單加個餅乾，卻像去超商買口香糖要經過海關 X 光機，使程式碼變得肥大且不必要。

三、 最終架構設計黃金法則
-----------------------------------------------------------------------------
1. 容量（Capacity）是「靜態上限設定」：
   允許被調整，因此適合配置完整的 Getter + Setter。
2. 數量（Size）是「動態行為結果」：
   它的數字是透過 `deposit` / `withdraw` 的動作自動產生的。對外應保持唯讀（僅 Getter），
   對內直接安全地操作私有變數（`self._size`），才能確保控制權永遠掌握在商業邏輯手裡！
"""