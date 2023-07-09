import typer
from peewee import *
from models import create_tables
from commands import restaurant , users ,food , cart , order
from services.authentication import UserSession, AuthenticationService
# from services.restaurant import RestaurantServices 
# from services.exception import FoodieExit
# from services.food import FoodServices
# from services.cart import CartService


app = typer.Typer()

user_session = users.user_session
auth = users.auth


app.add_typer(restaurant.app, name="restaurant")
app.add_typer(users.app, name="users")
app.add_typer(food.app, name="food")
app.add_typer(cart.app, name="cart")
app.add_typer(order.app, name="order")


if __name__ == "__main__":
    create_tables()
    with user_session:
        auth.load_session()
        app()