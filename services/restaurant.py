from models import Restaurant
from rich.console import Console
from rich.table import Table

console=Console()

class RestaurantServices:
    def add(self,name:str,address:str):
        place=Restaurant.create(name=name,address=address)
        print(f"{place.name} New Restaurant has been addedd!")

    def remove(self,name:str):
        place=Restaurant.get(name=name)
        place.delete_instance()
        print(f"{place.name} Restaurant has been removed")

    def display(self):
        place=Restaurant.select()
        table=Table("sl.no","Name","Address")

        for i,place in enumerate(place):
            table.add_row(str(i+1),place.name,place.address)

        console.print(table)