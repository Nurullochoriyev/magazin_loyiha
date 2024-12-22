
from mahsulot import Mahsulot

class Dokon:
    def __init__(self, nomi, balansi):
        self.nomi = nomi
        self.balansi = balansi
        self.mahsulot_bazasi = []
        self.istorya = []

    def add_mahsulot(self, mahsulot):
        self.mahsulot_bazasi.append(mahsulot)
        print(f"{mahsulot.nomi} qo'shildi.")

    def del_mahsulot(self, mahsulot):
        if mahsulot in self.mahsulot_bazasi:
            self.mahsulot_bazasi.remove(mahsulot)
            print(f"{mahsulot.nomi} o'chirildi.")
        else:
            print("Bunday mahsulot mavjud emas.")

    def korsat_barcha_mahsulotlar(self):
        print("Do‘kondagi mahsulotlar:")
        for i, mahsulot in enumerate(self.mahsulot_bazasi, 1):
            print(
                f"{i}. Nomi: {mahsulot.nomi}, Narxi: {mahsulot.narxi} so'm/kg, Yaroqlilik muddati: {mahsulot.mudati}")
