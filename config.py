import os

class TeleInfo():
    API_ID = int(os.environ["API_ID"])    # from https://my.telegram.org/app
    API_HASH = os.environ["API_HASH"]     # from https://my.telegram.org/app
    BOT_TOKEN = os.environ["BOT_TOKEN"]    # from @botfather
