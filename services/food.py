from models import Food,Restaurant
import peewee as pwee
from rich.console import Console
from rich.table import Table

console=Console()


class FoodServices:
    def add_fooditem(self,name:str,price:float,restaurant:str,quantity:int=0):
        try:
            r = Restaurant.get(name=restaurant)
            item=Food.create(name=name,price=price,restaurant=r,quantity=quantity)
        except pwee.IntegrityError:
            item: Food = Food.get(name=name)
            item.update_fooditem(price)
            item.update(restaurant)

        print(f"{item.name} New Food_Item has been addedd!")

    def remove_fooditem(self,name:str):
        try:

            item=Food.get(name=name)
            item.delete_instance()
            print(f"{item.name}  has been removed")
        except Food.DoesNotExist:
            print(f"Food '{name}' does not exist.")


    def display_fooditem(self):
        item=Food.select()
        table=Table("sl.no","Name","Price","Restaurant","quantity")
    
        for i,item in enumerate(item):
            table.add_row(f"{i+1}",item.name,f"Rs.{item.price}",item.restaurant.name,item.quantity)

        console.print(table)
