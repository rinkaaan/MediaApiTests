import openapi_client
from dotenv import load_dotenv
from faker import Faker

load_dotenv()
configuration = openapi_client.Configuration(
    host="http://localhost:34200",
)

api = openapi_client.ApiClient(configuration)
albumApi = openapi_client.AlbumApi(api)
fake = Faker()
