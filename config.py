import os

class TeleInfo():
    API_ID = int(os.environ.get("APP_ID", 12345))        # from https://my.telegram.org/app
    API_HASH = os.environ.get("API_HASH", None)          # from https://my.telegram.org/app
    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)     # from @botfather
