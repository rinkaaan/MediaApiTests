import openapi_client
from dotenv import load_dotenv
from faker import Faker

from models.base import Base
from nguylinc_python_utils.sqlalchemy import init_sqlite_db

load_dotenv()
configuration = openapi_client.Configuration(
    host="http://127.0.0.1:34200",
)

api = openapi_client.ApiClient(configuration)
albumApi = openapi_client.AlbumApi(api)
mediaApi = openapi_client.MediaApi(api)
fake = Faker()
session = init_sqlite_db(Base, "/Volumes/workplace/Media/MediaApi/api/sqlite.db")
