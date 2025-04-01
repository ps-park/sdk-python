## Create withdrawal request

```python
import uuid
from pspark import PSPark
from pspark.exceptions import ResponseValidationException
from pspark.requests import WithdrawalRequest, Details
from pspark.requests.details_dto import *


sdk = PSPark(jwt_key='jwt-key', api_key='api-key')

try:
    request = WithdrawalRequest(
        wallet_id="991D3240-4E74-44F8-991C-A6DA6D20F751",
        reference=str(uuid.uuid4()),
        amount=200,
        account="4111111111111111",
        details=Details(
            customer=Customer(
                first_name="First name",
                last_name="Last name",
            ),
            bank=Bank(
                id="Bank id",
                name="Bank name",
            ),
        ),
    )

    response = sdk.create_withdrawal(request)

    # Your business logic
except ResponseValidationException as e:
    print(f'Error message: {e.message}. Error code: {e.code}.')
```
