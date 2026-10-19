class Product:
    name:str=""
    price:int=0
    stock:int=0
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def __str__(self):
        return f"{self.name} - Price: {self.price} - Stock: {self.stock}"
class Shop:
    products:list[Product]
    balance:int=0
    def __init__(self,balance):
        self.products=[]
        self.balance=balance
    