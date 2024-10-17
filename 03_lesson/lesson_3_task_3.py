from address import Address
from mailing import Mailing

from_address = Address(414051, "Астрахань", "Адмирала Нахимова", "107А", 75)
to_address = Address(111673, "Москва", "Новокосинская", "13", 123)

mailing = Mailing(to_address, from_address, 400, 1234567)

print(mailing)