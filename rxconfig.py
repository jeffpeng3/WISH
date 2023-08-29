import reflex as rx
from dotenv import load_dotenv
from os import environ


load_dotenv()

print(f"http://{environ['address']}:3000")

class WishConfig(rx.Config):
    pass


config = WishConfig(
    app_name="WISH",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    api_url=f"http://{environ['address']}:8000",
    deploy_url=f"http://{environ['address']}:3000"
)
