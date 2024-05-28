import requests
from requests import Response
import Page_object.config
from typing import Optional


class APIInterface:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    def _get(self, endpoint: str, params=None) -> Response:
        return requests.get(Page_object.config.api.url + endpoint, headers=self.headers, params=params)

    def _post(self, endpoint: str, json=None, timeout: int = None, files: dict = None, data: dict = None) -> Response:
        return requests.post(Page_object.config.api.url + endpoint, json=json, data=data, headers=self.headers, files=files, timeout=timeout)

    def _put(self, endpoint: str, json=None, body=None) -> Response:
        return requests.put(Page_object.config.api.url + endpoint, data=body, json=json, headers=self.headers)

    def _delete(self, endpoint: str, params: Optional[dict]=None, body=None) -> Response:
        return requests.delete(Page_object.config.api.url + endpoint, data=body, headers=self.headers, params=params)
