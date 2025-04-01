## Request to check balance

```python
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import BalanceRequest


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
    request = BalanceRequest(wallet_id="08a03be1-aefa-4695-8186-b52411b4f240")

    response = sdk.get_balance(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
