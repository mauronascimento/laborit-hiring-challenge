from decouple import config

USER_DB = config("USER_DB", default=None)
PASSWORD_DB = config("PASSWORD_DB", default=None)
URL_DB = config("URL_DB", default=None)
NAME_DB = config("NAME_DB", default=None)
PORT_DB = config("PORT_DB", default=None)

DB_URL = f"mysql+pymysql://{USER_DB}:{PASSWORD_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}"

