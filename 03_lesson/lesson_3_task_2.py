from smartphone import Smartphone

catalog = [
    Smartphone("IPhone", "16 Pro Max", "+79998885533"),
    Smartphone("Honor", "S10 Note", "+79606677733"),
    Smartphone("Samsung", "Galaxy S21", "+79178800022"),
    Smartphone("HUAWEI", "Mate X3", "+79371234567"),
    Smartphone("Xiaomi", "POCO C40", "+79059876543")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.user_number}")