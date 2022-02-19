import requests
from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA


def test_getting_post():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200)        # Валидируем статус код
    response.validate_json(POST_SCHEMA)     # Json пришедший по API валидируем с помощью jsonschema
    response.assert_len_json(3)

