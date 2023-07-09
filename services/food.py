from models import Food
import peewee as pwee
from rich.console import Console
from rich.table import Table

console=Console()


class FoodServices:
    def add_fooditem(self,name:str,price:float,restaurant:str):
        try:
            item=Food.create(name=name,price=price,restaurant=restaurant)
        except pwee.IntegrityError:
            item: Food = Food.get(name=name)
            item.update_fooditem(price)
            item.update(restaurant)

        print(f"{item.name} New Food_Item has been addedd!")

    def remove_fooditem(self,name:str):
        item=Food.get(name=name)
        item.delete_instance()
        print(f"{item.name}  has been removed")

    def display_fooditem(self):
        item=Food.select()
        table=Table("sl.no","Name","Price","Restaurant")
    
        for i,item in enumerate(item):
            table.add_row(f"{i+1}",item.name,f"Rs.{item.price}",item.restaurant)

        console.print(table)
