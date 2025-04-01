## Request to get currency rates

```python
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import RateRequest


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
    request = RateRequest("DOGE", "USD")

    response = sdk.get_rates(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
