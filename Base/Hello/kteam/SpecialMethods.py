'''
    Phương thức đặc biệt là các phương thức có tên phương thức kiểu
    __Tên phương thức__

'''

'''
    Ví dụ: Ngoài __init__
    1) __str__ (Nó giống như phương thức ToString() trong C#)
    2) __repr__ (Là anh em họ của __str__)
    --> Nếu trong class có cả 2 phương thức trên
     thì hàm print ưu tiên dùng __str__
    , còn trên interactive prompt không dùng hàm print thì sẽ ưu tiên __repr__
    
    __str__ -> Chi tiết
    __repr__ -> Giá trị
    
'''


class SieuNhan:
    suc_manh = 50

    def __init__(self, ten, vukhi, mausac):
        self.ten = ten
        self.vukhi = vukhi
        self.mausac = mausac

    def __str__(seft):
        return 'Đây là {}, sử dụng {}'.format(seft.ten, seft.vukhi, seft.mausac)

    def __repr__(seft):
        return 'Tên: {}\nVũ khí: {}\nMàu sắc: {}'.format(seft.ten, seft.vukhi, seft.mausac)


SN_A = SieuNhan("Siêu nhân đỏ", "Kiếm", "Đỏ")
print(SN_A)

print('%s' % SN_A)
print('%r' % SN_A)
# Hàm __len__
s = 'Nguyễn Công Bình'
print(len(s))
print(s.__len__())
# __add__
print(int.__add__(3, 4))
print(str.__add__("Bình ", "Nguyễn Công"))
