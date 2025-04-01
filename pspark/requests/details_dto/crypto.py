from typing import Optional
from dataclasses import dataclass
from ..abstract_request import AbstractRequest


@dataclass
class Crypto(AbstractRequest):
    memo: Optional[str] = None
