# Python có thể tự động hiểu kiểu dữ liệu
x = 2
print(x)
# Cách viết tên biến
'''
    - Tên biến phải bắt đầu bằng chữ cái hoặc ký tự gạch dưới _
    - Phân biệt chữ hoa, chữ thường
    - Tên biến không thể là 1 từ khóa của python
    - Cách viết tên biến có nhiều từ (nên dùng)
        + myCarName
        + MyCarName
        + my_car_name
'''
X = "Hello"
print(X)
# Có thể chỉ định kiểu dữ liệu của biến bằng cách ép kiểu
xx = str(3)
y = int(3)
z = float(3)
print(xx)
print(y)
print(z)
# Kiểm tra kiểu dữ liệu
print(type(xx))
print(type(y))
# Cách gán nhiều giá trị cho bến
x, y, z = 3, 4, 5
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
#  Unpack (Giải nén 1 bộ dữ liệu)
# List: Có thể thay thay đổi dữ liệu
fruits = ["apple", "banana", "cherry"]
# Tuple: Không thể thay đổi dữ liệu
fruits = ("apple", "banana", "cherry")
print(fruits)
x, y, z = fruits
# Hiển thị dữ liệu trên cùng 1 dòng (có dấu phân cách)
print(x, y, z)
# Nối giá trị chuỗi -> Xuất ra
print(x + y + z)
# Xuất ra giá trị của 1 biểu thức toán (Các toán hạng phải cùng kiểu dữ liệu)
x = 4
y = 2.67
print(x + y)
# Một trường hợp cần lưu ý
x = 5
y = "John"
print(str(x) + y)

# Phạm vi của biến (toàn cục và cục bộ)
# Các cách khai báo biến toàn cục
# C1:
x = 4


def myLocalFunc():
    global yyy
    yyy = "fantastic"


# myLocalFunc()

print("Global 1", x)
print("Global 2 " + yyy)
