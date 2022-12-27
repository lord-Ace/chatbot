class Items:
    def __init__(self, name: str, price: float, quantity=0, pay_rate=0.8):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.pay_rate = pay_rate
    
    def total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price


polo = str(input("do you want to apply you discount or use built in discount manager? (Yes or No): ")).lower()
rate = int()
if polo == "yes":
    rate = 0.9
else:
    rate = 0.0
item1 = Items("phone", 100, 1, pay_rate=rate)
item2 = Items("Laptop", 1000, 3)
item3 = Items("Cable", 10, 5)
item4 = Items("Mouse", 50, 5)
item5 = Items("Keyboard", 75, 5)
