```python
from fastapi import FastAPI

from furiousapi.db import FuriousEntityError
from furiousapi.api.exception_handling import furious_exception_handler

app = FastAPI()
app.add_exception_handler(FuriousEntityError, furious_exception_handler)
```