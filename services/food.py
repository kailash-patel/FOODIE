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

    def list(self):
        foods = Food.select()

        if foods.count() == 0:
            print("No food items found.")
            return

        table = Table("sl.No.", "Name", "Price",  "Food-id")
        for i, food in enumerate(foods):
            table.add_row(
                f"{i + 1}",
                food.name,
                str(food.price),
                str(food.id),
            )
        
        console.print("List of all food items:")
        console.print(table)
