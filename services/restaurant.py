from models import Restaurant ,Food
from rich.console import Console
from rich.table import Table
import peewee as pwee

console=Console()

class RestaurantServices:
    def add(self,name:str,address:str):
        place=Restaurant.create(name=name,address=address)
        print(f"{place.name} New Restaurant has been addedd!")

    def remove(self,name:str):
        try:

            place=Restaurant.get(name=name)
            place.delete_instance()
            print(f"Restaurant '{place.name}' has been removed from the restaurant list. ")
        except Restaurant.DoesNotExist:
            print(f"{place.name} Restaurant does not exist")

    def display(self):
        place=Restaurant.select()
        table=Table("sl.no","Name","Address")

        for i,place in enumerate(place):
            table.add_row(str(i+1),place.name,place.address)

        console.print(table)

    def list_foods(self, restaurant_name: str):
        while True:
            try:
                restaurant = Restaurant.get(name=restaurant_name)
                foods = Food.select().where(Food.restaurant == restaurant)

                if foods.count() == 0:
                    print(f"No food items found for restaurant '{restaurant_name}'.")
                    return

                table = Table("sl.No.", "Name", "Price", "Is Veg", "Food-id")
                for i, food in enumerate(foods):
                    table.add_row(
                        f"{i + 1}",
                        food.name,
                        str(food.price),
                        "Yes" if food.is_veg else "No",
                        str(food.id),
                    )

                console.print(f"Food items for restaurant '{restaurant_name}':")
                console.print(table)
                break
            except Restaurant.DoesNotExist:
                print(f"Restaurant '{restaurant_name}' does not exist.")
                restaurant_name = input("Enter the restaurant name again: ")
