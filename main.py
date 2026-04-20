import datetime
import getpass
import hashlib
import os

class Diary:
    def __init__(self):
        self.diary = {}

    def add_entry(self, date, entry):
        self.diary[date] = entry

    def view_entries(self, date=None):
        if date:
            return self.diary.get(date)
        else:
            return self.diary

    def delete_entry(self, date):
        if date in self.diary:
            del self.diary[date]
        else:
            print("No entry found for this date.")

    def encrypt_entry(self, date, entry):
        encrypted_entry = hashlib.sha256((entry + str(date)).encode()).hexdigest()
        self.diary[date] = encrypted_entry

    def decrypt_entry(self, date):
        encrypted_entry = self.diary.get(date)
        if encrypted_entry:
            decrypted_entry = hashlib.sha256((encrypted_entry + str(date)).encode()).hexdigest()
            return decrypted_entry
        else:
            return None

    def save_diary(self, filename):
        with open(filename, 'w') as f:
            for date, entry in self.diary.items():
                f.write(f"{date}:{entry}\n")

    def load_diary(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for line in f.readlines():
                    date, entry = line.strip().split(":")
                    self.diary[date] = entry
        else:
            print("No diary file found.")

def main():
    diary = Diary()
    while True:
        print("1. Yangi yozuv qo'shish")
        print("2. Sana bo'yicha qidirish")
        print("3. Parol bilan ochish")
        print("4. Chiqish")
        choice = input("Izoh: ")
        if choice == "1":
            date = input("Sana (YYYY-MM-DD): ")
            entry = input("Yozuv: ")
            diary.encrypt_entry(date, entry)
            diary.save_diary("diary.txt")
        elif choice == "2":
            date = input("Sana (YYYY-MM-DD): ")
            print(diary.view_entries(date))
        elif choice == "3":
            password = getpass.getpass("Parol: ")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == "your_hashed_password":  # Qayta yozish kerak
                diary.load_diary("diary.txt")
                while True:
                    print("1. Sana bo'yicha qidirish")
                    print("2. Chiqish")
                    choice = input("Izoh: ")
                    if choice == "1":
                        date = input("Sana (YYYY-MM-DD): ")
                        print(diary.view_entries(date))
                    elif choice == "2":
                        break
            else:
                print("Parol noto'g'ri.")
        elif choice == "4":
            break
        else:
            print("Izoh: ")

if __name__ == "__main__":
    main()
```

Buning uchun sizga quyidagilar kerak:

1. "your_hashed_password" ni qayta yozib, uning o'rniga parolni kiritib, dasturni ishga tushiring.
2. Dastur ishga tushgach, parolni kiritib, sana bo'yicha qidirish yoki chiqishni tanlang.
3. Sana bo'yicha qidirishni tanlang, keyin sana kiritib, yozuvni ko'rasiz.
4. Chiqishni tanlang, dastur tugaydi.
