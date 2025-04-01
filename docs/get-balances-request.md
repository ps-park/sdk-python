## Request to check balance

```python
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import BalancesRequest


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
    request = BalancesRequest()

    response = sdk.get_balances(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
