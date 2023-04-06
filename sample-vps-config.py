import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "6015933908:AAG9tDZkkz-LG2Tx_Lz3KZGm0oeaMrGzzno"
    APP_ID = 27885485
    API_HASH = "7dd9974c713787410beae4a295cc1e2d"
    TG_USER_SESSION = "AQAAzB4kZkggWqtCxwkQtOA6sUjnDWr-SKjHdm1mwrJIJBVEW2hawVirR3GBn-mvpbt3FRbgUTYQGMNQ4qtvztdLjl57M2lKTAbxwP91a_nq2Lsa2oyRLp6jigtCuz5ZdYpzS9s8--W6ljalJeT6vU_n-iYqmlKcKmZ-pKR1E5tM_jwVaHTdgj9y6CyKIyXBe8h0PUJ4mJ5axKIjR4NcBfPO_iIRSo6x1jnVrr01u5FlY2MGDboUf8tqzrhXfFxp1Ps4QnNrmGoHliHAnKRYACp423utR_-4epSCTRf_jUJICs7Y3gS0HLxgl1qBUphfzFIO145GCeNxHgrswT90AqtwAAAAAVGSwuQA"
    DB_URI = "mongodb+srv://sanmart02:sanmart02@cluster0.ktbxuq6.mongodb.net/?retryWrites=true&w=majority"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
