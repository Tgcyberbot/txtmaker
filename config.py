import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6664755882:AAG0qJHptIXS4YaB6-n-8B7cejl_thmv800")
    APP_ID = int(os.environ.get("APP_ID", 24131567))
    API_HASH = os.environ.get("API_HASH", "7bf12fc2ec81ba350bca34c014549bee")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
