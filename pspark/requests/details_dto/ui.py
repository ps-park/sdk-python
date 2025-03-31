from typing import Optional
from dataclasses import dataclass
from ..abstract_request import AbstractRequest


@dataclass
class Ui(AbstractRequest):
    language: Optional[str] = None
