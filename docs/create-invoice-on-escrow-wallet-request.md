## Create Invoice request

```python
import uuid
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import InvoiceRequest, Details
from pspark.requests.details_dto import *


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
    # '991D3240-4E74-44F8-991C-A6DA6D20F751' - Invoice wallet (for example: EUR)
    # 'DADC983B-6D9A-41C9-BC21-A17667CAF8D4' - Payment wallet ID of the payment wallet (which represents a payment currency,
    # for example USDT).
    
    # You can retrieve all wallet ids which you have created by using get-balances-request (see doc example). But take
    # into account that get-balance-request will have a request rate limit, so you should temporarily cache this
    # data
    
    request = InvoiceRequest(
        wallet_id="991D3240-4E74-44F8-991C-A6DA6D20F751",
        reference=str(uuid.uuid4()),
        amount=100,
        details=Details(
            escrow_payment=EscrowPayment(
                payment_wallet_id="DADC983B-6D9A-41C9-BC21-A17667CAF8D4"
            ),
        ),
        title="Order #15223",
        callback_url="https://your-domain.io/calback-url",
        return_url="https://your-domain.io/return-url",
    )

    response = sdk.create_invoice(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
