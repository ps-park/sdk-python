## Request to check Transaction status

```python
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import TransactionRequest


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
    request = TransactionRequest(
        wallet_id="08a03be1-aefa-4695-8186-b52411b4f240",
        reference="7555e4a7-f464-43b1-859e-950f445dc7d4",
    )

    response = sdk.get_transaction_status(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
