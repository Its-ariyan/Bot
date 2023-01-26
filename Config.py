import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', 0))
    except ValueError:
        raise Exception("Your OWNER_ID is not a valid integer.")
    DATABASE_URL = os.environ.get('DATABASE_URL')
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 23842900
    API_HASH = "d21e95895cf2a5b83b0167fdd3b6e541"
    BOT_TOKEN = "5893689063:AAEVtWvopw-dTw0xQRa-o0BU8CRlTCBh1Is"
    DATABASE_URL = "postgres://nmjrboas:4UpeJ89pSZMw8dkK5T8XoFIZR50HxTw6@kashin.db.elephantsql.com/nmjrboas"
    MUST_JOIN = "NixaWorld"
    OWNER_ID = 5761513990
