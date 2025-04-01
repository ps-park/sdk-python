## Create Address request

```python
import uuid
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import AddressRequest


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
    request = AddressRequest(
        wallet_id="08a03be1-aefa-4695-8186-b52411b4f240",
        reference=str(uuid.uuid4()),
    )

    response = sdk.create_address(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
