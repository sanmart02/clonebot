#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "6015933908:AAG9tDZkkz-LG2Tx_Lz3KZGm0oeaMrGzzno"

    # Get from my.telegram.org
    APP_ID = 27885485

    # Get from my.telegram.org
    API_HASH = "7dd9974c713787410beae4a295cc1e2d"

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
