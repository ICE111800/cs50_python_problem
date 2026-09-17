import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar2 = Jar(10)
    assert jar2.capacity == 10

    jar3 = Jar(0)
    assert jar3.capacity == 0

    # 測試不合法的容量是否會報錯
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises((ValueError, TypeError)):
        Jar("abc")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    
    jar.deposit(1)
    assert str(jar) == "🍪"
    
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    jar.deposit(0)
    assert jar.size == 0

    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(7)
    assert jar.size == 12

    # 測試存入超過容量是否正確報錯
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(12)
    jar.deposit(10)
    
    jar.withdraw(4)
    assert jar.size == 6

    jar.withdraw(6)
    assert jar.size == 0

    # 測試提領過多是否正確報錯
    with pytest.raises(ValueError):
        jar.withdraw(1)


"""
# 一次測試多種合法的容量
@pytest.mark.parametrize("capacity", [0, 1, 12, 100])
def test_init(capacity):
    jar = Jar(capacity)
    assert jar.capacity == capacity

# 測試不合法的容量（包含負數，甚至是字串或小數等異常型別）
@pytest.mark.parametrize("invalid_capacity", [-1, -100, "abc", 3.5])
def test_init_invalid(invalid_capacity):
    with pytest.raises((ValueError, TypeError)):
        Jar(invalid_capacity)

# 測試 str
@pytest.mark.parametrize("n, expected_str", [
    (0, ""),
    (1, "🍪"),
    (5, "🍪🍪🍪🍪🍪"),
    (12, "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"),
])
def test_str(n, expected_str):
    jar = Jar()
    if n > 0:
        jar.deposit(n)
    assert str(jar) == expected_str

# 參數化測試：不同的存入情境
@pytest.mark.parametrize("initial_capacity, deposit_n, expected_size", [
    (12, 0, 0),
    (12, 5, 5),
    (12, 12, 12),
])
def test_deposit(initial_capacity, deposit_n, expected_size):
    jar = Jar(initial_capacity)
    jar.deposit(deposit_n)
    assert jar.size == expected_size

# 參數化測試：存入超過容量時是否正確報錯
@pytest.mark.parametrize("initial_capacity, deposit_n", [
    (10, 11),
    (5, 6),
    (12, 15),
])
def test_deposit_invalid(initial_capacity, deposit_n):
    jar = Jar(initial_capacity)
    with pytest.raises(ValueError):
        jar.deposit(deposit_n)

# 測試成功提領
@pytest.mark.parametrize("capacity, deposit_n, withdraw_n, expected_size", [
    (12, 10, 4, 6),     # 放 10 拿 4，剩 6
    (12, 5, 5, 0),      # 放 5 拿 5，全拿光剩 0
    (20, 15, 10, 5),    # 放 15 拿 10，剩 5
])
def test_withdraw(capacity, deposit_n, withdraw_n, expected_size):
    jar = Jar(capacity)
    jar.deposit(deposit_n)
    jar.withdraw(withdraw_n)
    assert jar.size == expected_size

# 測試提領過多而報錯
@pytest.mark.parametrize("capacity, deposit_n, withdraw_n", [
    (12, 5, 6),     # 只有 5 片，卻想拿 6 片
    (12, 0, 1),     # 0 片，想拿 1 片
    (10, 10, 11),   # 10 片，想拿 11 片
])
def test_withdraw_invalid(capacity, deposit_n, withdraw_n):
    jar = Jar(capacity)
    jar.deposit(deposit_n)
    with pytest.raises(ValueError):
        jar.withdraw(withdraw_n)
"""

    


























# def test_init():
#     jar = Jar()
#     assert jar.capacity == 12

#     jar = Jar(12)
#     assert jar.capacity == 12

#     jar = Jar(100)
#     assert jar.capacity == 100

#     # 測試傳入負數容量時，是否會正確引發 ValueError
#     jar = Jar(-1)
#     with pytest.raises(ValueError):
#         Jar(-1)

# def test_str():
#     jar = Jar()
#     assert str(jar) == ""
#     jar.deposit(1)
#     assert str(jar) == "🍪"
#     jar.deposit(11)
#     assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

# def test_deposit():
#     jar = Jar(12)
#     jar.deposit(5)
#     assert jar.size == 5

#     jar.deposit(7)
#     assert jar.size == 12

#     # 測試超過容量時是否會引發 ValueError
#     with pytest.raises(ValueError):
#         jar.deposit(1)  # 滿了再存會報錯


# def test_withdraw():
#     jar = Jar(12)
#     jar.deposit(10) # 先放 10 片進去

#     jar.withdraw(3) # 拿走 3 片
#     assert jar.size == 7

#     # 測試拿超過現有庫存時是否會引發 ValueError
#     with pytest.raises(ValueError):
#         jar.withdraw(10)    # 剩下 7 片，卻想拿 10 片，應該要報錯