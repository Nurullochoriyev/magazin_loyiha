

class User:
    def __init__(self, ism, tel_raqam, karta_raqam, karta_parol, balans):
        self.ism = ism
        self.tel_raqam = tel_raqam
        self.karta_raqam = karta_raqam
        self.karta_parol = karta_parol
        self.balans = balans

    def tekshir_balans(self):
        print(f"{self.ism}ning balansi: {self.balans} so'm")

    def yech_balans(self, summa):
        if self.balans >= summa:
            self.balans -= summa
            print(f"{summa} so'm balansingizdan yechildi. Qolgan balans: {self.balans} so'm")
            return True
        else:
            print("Balans yetarli emas!")
            return False
