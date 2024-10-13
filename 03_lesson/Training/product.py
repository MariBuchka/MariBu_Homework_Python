class Product:
    def __init__(self, name, price): # КОНСТРУКТОР описывает принимаемые параметры (сохраняет атрибуты объекта)
        self.name = name
        self.price = price

    def getName(self):  # МЕТОД возвращает название продукта
        return self.name

    def getPrice(self):  # МЕТОД возвращает цену продукта
        return self.price

    def getInfoProduct(self):  # МЕТОД возвращает строку с объединением названия и цены продукта
        return f"Product: {self.name},\nPrice: {self.price}"