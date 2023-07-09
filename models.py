"""
Peewee is a Python ORM (Object-Relational Mapping) library
This file contains all the neccessary database relationship required in the program

"""

from peewee import *
from services.exception import FoodieExit


#Creating Database Connection
db=SqliteDatabase("foodie.db")


class User(Model):
    username=CharField(unique=True)
    password=CharField()
    is_vegetarian = BooleanField(default=False)

    class Meta:
        database=db

class Restaurant(Model):
    name=CharField()
    address=CharField()


    class Meta:
        database=db

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.rating}"

    @staticmethod
    def add_restaurant(name: str, rating: float):
        Restaurant.create(name=name, rating=rating)

    @staticmethod
    def remove_restaurant(name: str):
        Restaurant.delete().where(Restaurant.name == name).execute()

    @staticmethod
    def display_restaurants():
        for restaurant in Restaurant.select():
            print(restaurant)

    def list_foods(self):
        foods = Food.select().where(Food.restaurant == self)
        for food in foods:
            print(food)




class Food(Model):
    name=CharField(unique=True)
    price=FloatField()
    restaurant=ForeignKeyField(Restaurant, backref='food_items')

    class Meta:
        database=db

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.price}"

    @staticmethod
    def availability(name: str, quantity: int):
        item =Food.get(name=name)
        if item.quantity < quantity:
            raise FoodieExit(f"Only {item.quantity} {name} available.")
        return item

    @staticmethod
    def pick_item(name: str, quantity: int):
        item = Food.availability(name, quantity)
        item.quantity = item.quantity - quantity
        item.save()

    @staticmethod
    def drop_item(name: str, quantity: int):
        item = Food.get(name=name)
        item.quantity = item.quantity + quantity
        item.save()

    def update_stock(self, price: int, quantity: int):
        self.update_price(price)
        self.update_quantity(quantity)
        self.save()
        print(f"{self.name} restocked!")

    def update_price(self, price: int):
        if self.price != price:
            self.price = price
            print(f"{self.name} price updated!")

    def update_quantity(self, quantity: int):
        self.quantity += quantity
        print(f"{self.name} quantity updated!")

class Cart(Model):
    user = ForeignKeyField(User)
    food_item = ForeignKeyField(Food)
    quantity = IntegerField()

    class Meta:
        database =db

    def add(self,quantity: int):
        self.quantity = self.quantity +quantity
        self.save()

    def remove(self, quantity: int):
        self.quantity = self.quantity - quantity
        self.save()
        if self.quantity == 0:
            self.delete_instance()


 
class Order(Model):
    user = ForeignKeyField(User)
    item = ForeignKeyField(Food)
    quantity = IntegerField()
    amount = FloatField()
    payment_mode =CharField()
    status =CharField(default="pending")

    class Meta:
        database = db

        


def create_tables():
    with db:
        db.create_tables([Restaurant,User,Food])


