import reflex as rx

class WishConfig(rx.Config):
    pass

config = WishConfig(
    app_name="WISH",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)