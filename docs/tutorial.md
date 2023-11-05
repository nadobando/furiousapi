# Tutorial: Building Your First API with FuriousAPI

In this tutorial, you will learn how to build a more comprehensive API with FuriousAPI. We'll expand on the Quick Start guide by adding more functionality to our `Item` model.

## Prerequisites

Before starting this tutorial, you should have:

- Completed the [Quick Start](./quickstart.md) guide.
- Basic understanding of Python and FastAPI.
- FuriousAPI installed in your virtual environment.

## Step 1: Expand Your Model

Let's add more fields to our `Item` model to make it more interesting.

```python
# models.py
from sqlmodel import SQLModel, Field

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str = Field(default=None, nullable=True)
    price: float = Field(default=0)
    is_available: bool = Field(default=True)
```

## Step 2: Enhance Your Repository

Update your repository to handle more complex queries.

```python
# repository.py
from furiousapi.sqlmodel import SQLRepository
from .models import Item


class ItemRepository(SQLRepository[Item]):

    async def set_item_availability(self, id_: int, status: bool):
        item = await self.get(id_)
        item.is_available = status
        self.session.add(item)
        await self.session.commit()

```

## Step 3: Update the Controller

Modify your `ItemController` to use the new repository methods.

```python
# controllers.py
import http
from fastapi import Depends, Path
from furiousapi.api import ModelController, action
from repository import ItemRepository


class ItemController(ModelController, prefix="/item", tags=["Items"]):
    repository = Depends(ItemRepository)

    @action("/{id}/set-availability/{status}", methods=[http.HTTPMethod.POST])
    async def get_available_items(self, id_=Path(alias="id"), status: bool = Path()):
        return await self.repository.set_item_availability(id_, status)
```

## Step 4: Test Your API

With your API updated, it's time to test the new functionality. Use tools like `httpx` or Postman to make requests to your endpoints and ensure everything works as expected.

## Conclusion

Congratulations! You've just expanded your API to handle more complex data and secured it with basic authentication. As you continue to develop with FuriousAPI, remember to refer to the documentation for guidance on more advanced features and best practices.
