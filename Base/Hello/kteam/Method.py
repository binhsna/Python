# regular methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


my_rectangle = Rectangle(4, 5)
area = my_rectangle.calculate_area()
print(area)


# class methods
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def calculate_area(self):
        return 3.14 * self.radius ** 2


circle = Circle.from_diameter(10)
area = circle.calculate_area()
print(area)


# static methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


result1 = MathUtils.add(5, 3)
print(result1)

result2 = MathUtils.multiply(4, 6)
print(result2)


# 
class sieunhan:
    suc_manh = 50

    def __init__(self, _ten, _vukhi, _mausac):
        self.ten = _ten
        self.vukhi = _vukhi
        self.mausac = _mausac

    # regular methods là phương thức có seft, thuộc class và được gọi bởi object
    def calculate_area(self):
        return self.ten

    # Phương thức thường của lớp, không phụ thuộc vào object
    @classmethod
    def cap_nhat_suc_manh(cls, smanh):
        cls.suc_manh = smanh

    # Thường những phương thức xử lý thế này có tên là from...
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vukhi, mausac = new_lst
        return cls(ten, vukhi, mausac)

    # Phương thức static
    @staticmethod
    def bien_hinh():
        print("1, 2 ,3. Siêu nhân biến hình")


sieunhana = sieunhan("Bình", "kiếm", "Đỏ")
sieunhan.cap_nhat_suc_manh(30)

print(sieunhan.suc_manh)
info_str = "do - Kiem - Do"
sieunhanb = sieunhan.from_string(info_str)
print(sieunhanb.__dict__)

sieunhan.bien_hinh()
