"""
Peewee is a Python ORM (Object-Relational Mapping) library
This file contains all the neccessary database relationship required in the program

"""

from peewee import *
from services.exception import ShopYooExit


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


class Food(Model):
    name=CharField(unique=True)
    price=FloatField()
    restaurant=ForeignKeyField(Restaurant, backref='food_items')

    class Meta:
        database=db

    @staticmethod
    def create_food_item(name: str, price: float):
        try:
            print("Select a Restaurant:")
            restaurants = Restaurant.select()
            for i, restaurant in enumerate(restaurants):
                print(f"{i + 1}. {restaurant.name}")
            choice = int(input("Enter the number of the restaurant: "))
            if choice < 1 or choice > len(restaurants):
                print("Invalid choice!")
                return
            restaurant = restaurants[choice - 1]
            Food.create(name=name, price=price, restaurant=restaurant)
            print("Food item created successfully!")
        except IntegrityError:
            print("Food item name already exists!")

            


def create_tables():
    with db:
        db.create_tables([Restaurant,User,Food])


