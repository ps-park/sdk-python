from typing import Optional
from dataclasses import dataclass
from ..abstract_request import AbstractRequest


@dataclass
class EscrowPayment(AbstractRequest):
    payment_wallet_id: Optional[str] = None
