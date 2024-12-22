
from dokon import Dokon
from mahsulot import Mahsulot
from user import User


dokon = Dokon("Korzinka", 100_000_000)


dokon.add_mahsulot(Mahsulot("Mandarin", 20000, "10 kun"))
dokon.add_mahsulot(Mahsulot("Nok", 15000, "7 kun"))
dokon.add_mahsulot(Mahsulot("Piyoz", 5000, "30 kun"))
dokon.add_mahsulot(Mahsulot("Sabzi", 7000, "25 kun"))
dokon.add_mahsulot(Mahsulot("Olma", 12000, "15 kun"))
dokon.add_mahsulot(Mahsulot("Anor", 18000, "10 kun"))


users = [
    User("Ali", "+998901234567", "8600123456789012", "1234", 200_000),
    User("Vali", "+998901234568", "8600123456789013", "4321", 150_000),
    User("vali2", "+998901234569", "8600123456789014", "5678", 300_000),
]


while True:
    print("\nFoydalanuvchilar:")
    for idx, user in enumerate(users, 1):
        print(f"{idx}. {user.ism} - {user.tel_raqam}")
    print("4. Chiqish")

    tanlangan_foydalanuvchi = input("Foydalanuvchini tanlang (raqam kiriting): ")

    if tanlangan_foydalanuvchi == "4":
        print("Dasturdan chiqildi. Xush kelibsiz!")
        break

    try:
        tanlangan_foydalanuvchi = int(tanlangan_foydalanuvchi) - 1
        if tanlangan_foydalanuvchi < 0 or tanlangan_foydalanuvchi >= len(users):
            print("Noto‘g‘ri raqam kiritildi. Qaytadan tanlang.")
            continue

        user = users[tanlangan_foydalanuvchi]
        print(f"\nXush kelibsiz, {user.ism}!")

        # Foydalanuvchi harid qiladi
        while True:
            print("\n1: Mahsulotlarni ko‘rish")
            print("2: Harid qilish")
            print("3: Balansni ko‘rish")
            print("4: Orqaga qaytish")
            tanlov = input("Tanlang: ")

            if tanlov == "1":
                dokon.korsat_barcha_mahsulotlar()

            elif tanlov == "2":
                dokon.korsat_barcha_mahsulotlar()
                haridlar = []
                umumiy_summa = 0

                while True:
                    mahsulot_tanlash = input(
                        "Harid qilish uchun mahsulot raqamini kiriting (yoki '0' chiqish uchun): ")
                    if mahsulot_tanlash == "0":
                        break

                    try:
                        mahsulot_tanlash = int(mahsulot_tanlash) - 1
                        if mahsulot_tanlash < 0 or mahsulot_tanlash >= len(dokon.mahsulot_bazasi):
                            print("Noto‘g‘ri raqam! Qaytadan tanlang.")
                            continue

                        mahsulot = dokon.mahsulot_bazasi[mahsulot_tanlash]
                        miqdor = input(
                            f"{mahsulot.nomi}dan qancha kg olmoqchisiz? (Masalan: 2.5): ")
                        try:
                            miqdor = float(miqdor)
                            narx = mahsulot.narxi * miqdor
                            umumiy_summa += narx
                            haridlar.append((mahsulot.nomi, miqdor, narx))
                            print(
                                f"{miqdor} kg {mahsulot.nomi} qo‘shildi. Narxi: {narx} so'm.")
                        except ValueError:
                            print("Iltimos, miqdorni to‘g‘ri kiriting.")
                    except ValueError:
                        print("Iltimos, to‘g‘ri raqam kiriting.")

                # Haridlarni yakunlash
                if haridlar:
                    print("\nSizning haridingiz:")
                    for nomi, miqdor, narx in haridlar:
                        print(f"{nomi}: {miqdor} kg - {narx} so'm")
                    print(f"Umumiy summa: {umumiy_summa} so'm")

                    # Balansdan yechish
                    print("\nTo‘lov jarayoni:")
                    if user.yech_balans(umumiy_summa):
                        print("To‘lov amalga oshirildi. Rahmat!")
                    else:
                        print("To‘lov amalga oshirilmadi. Balans yetarli emas.")
                else:
                    print("Siz hech narsa sotib olmadingiz.")

            elif tanlov == "3":
                user.tekshir_balans()

            elif tanlov == "4":
                print("Orqaga qaytildi.")
                break

            else:
                print("Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")

    except ValueError:
        print("Noto‘g‘ri tanlov. Iltimos, raqam kiriting.")
