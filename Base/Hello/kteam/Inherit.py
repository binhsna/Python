class SieuNhan:
    suc_manh = 50

    def __init__(self, ten, vukhi, mausac):
        self.ten = ten
        self.vukhi = vukhi
        self.mausac = mausac


class SieuNhanKteam(SieuNhan):
    suc_manh = 40

    def __init__(self, ten, vukhi, mausac, sieuthu):
        # self.ten = ten
        # self.vukhi = vukhi
        # self.mausac = mausac
        super().__init__(ten, vukhi, mausac)
        self.sieuthu = sieuthu


Kteam_do = SieuNhanKteam("do", "cung", "do", "Rắn xanh")
print(Kteam_do.__dict__)
print(Kteam_do.suc_manh)
