# Thuộc tính của lớp
class sieunhan:
    suc_manh = 50
    so_thu_tu = 1
    stt = 1

    def __init__(self, _ten, _vukhi, _mausac):
        self.ten = _ten
        self.vukhi = _vukhi
        self.mausac = _mausac
        self.stt = sieunhan.so_thu_tu
        sieunhan.so_thu_tu += 1


sieunhana = sieunhan("Bình", "kiếm", "Đỏ")
sieunhanb = sieunhan("Bình", "kiếm", "Đỏ")

print("Tên của siêu nhân là: ", sieunhana.ten)
print("Siêu nhân màu: ", sieunhana.mausac)
print("Sử dụng vũ khí: ", sieunhana.vukhi)

# Cách 1
print(sieunhana.suc_manh)
# Cách 2
print(sieunhan.suc_manh)

print(sieunhan.stt)
print(sieunhanb.stt)
print(sieunhan.so_thu_tu)
