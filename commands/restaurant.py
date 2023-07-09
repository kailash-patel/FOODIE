import typer
from models import create_tables , Restaurant
from services.restaurant import RestaurantServices
from typing_extensions import Annotated

app=typer.Typer()

restaurant = RestaurantServices()

@app.command()
def add(name: Annotated[str, typer.Option(prompt=True)],
        address: Annotated[str, typer.Option(prompt=True)],):
        restaurant.add(name,address)

@app.command()
def remove(name: Annotated[str , typer.Option(prompt=True)]):
    restaurant.remove(name)

@app.command()
def display():
    restaurant.display()

@app.command()
def list_foods(res_name:Annotated[str,typer.Option(prompt=True)],):
     restaurant.list_foods(res_name)
     