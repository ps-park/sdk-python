from .http_exception import HttpException
from ..responces import HttpResponse


class HttpRedirectionException(HttpException):
    def __init__(self, url: str, response: HttpResponse):
        super().__init__(
            f"Redirect error occurred. Status code: {response.status_code}. URL: {url}"
        )
        self._response = response

    @property
    def response(self):
        return self._response
