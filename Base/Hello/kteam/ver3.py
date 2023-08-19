class sieunhan:
    def __init__(self, _ten, _vukhi, _mausac):
        self.ten = _ten
        self.vukhi = _vukhi
        self.mausac = _mausac

    def xin_chao(self):
        return "Xin chào, ta chính là " + self.ten


sieunhana = sieunhan("Bình", "kiếm", "Đỏ")

print("Tên của siêu nhân là: ", sieunhana.ten)
print("Siêu nhân màu: ", sieunhana.mausac)
print("Sử dụng vũ khí: ", sieunhana.vukhi)

# Cách 1
print(sieunhana.xin_chao())
# Cách 2
print(sieunhan.xin_chao(sieunhana))
