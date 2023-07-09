import typer
from models import create_tables , Food
from services.food import FoodServices
from typing_extensions import Annotated

app=typer.Typer()

food = FoodServices()

@app.command()
def add_fooditem(name: Annotated[str, typer.Option(prompt=True)],
    price: Annotated[float, typer.Option(prompt=True)],
    restaurant : Annotated[str, typer.Option(prompt=True)]):
        food.add_fooditem(name=name,price=price,restaurant=restaurant )

@app.command()
def remove_fooditem(name: Annotated[str,typer.Option(prompt=True)]):
        food.remove_fooditem(name=name)

@app.command()
def display_fooditem():
        food.display_fooditem()