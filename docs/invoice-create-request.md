## Create Invoice request

```python
import uuid
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import InvoiceRequest


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
   
    request = InvoiceRequest(
        wallet_id="991D3240-4E74-44F8-991C-A6DA6D20F751",
        reference=str(uuid.uuid4()),
        amount=50,
        callback_url="https://your-domain.io/calback-url",
        return_url="https://your-domain.io/return-url",
    )

    response = sdk.create_invoice(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
