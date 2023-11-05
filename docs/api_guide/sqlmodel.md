# SQLModel Integration with FuriousAPI

[SQLModel](https://sqlmodel.tiangolo.com/) is a library that bridges SQL databases with Python models
using [SQLAlchemy](https://www.sqlalchemy.org/) for database operations and
Pydantic for data validation. **FuriousAPI** leverages **SQLModel** to provide an ORM layer that is both powerful and
easy to use.
the **`furiousapi-sqlmodel`** extension integrates **SQLModel** to provide a seamless experience when working with **SQL**.

## Repository Pattern with SQLModel

The repository pattern in `FuriousAPI` abstracts away the data access layer. With the `furiousapi-sqlmodel` extension,
this pattern is implemented for SQL using SQLModel. This allows for a consistent CRUD interface and query
capabilities, abstracting away the specifics of SQL access.

## Setting up an SQLModel Repository

To set up a **SQLModel** repository in `FuriousAPI`, you need to define a model using SQLModel's `SQLModel` class and then
create a repository class that extends `SQLRepository`. The repository class will handle the data operations for the
model.

```python
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel, Field
from sqlmodel.ext.asyncio.session import AsyncSession

from furiousapi.api import ModelController
from furiousapi.sqlmodel import SQLRepository

# app_dependencies.py
engine = create_async_engine("sqlite+aiosqlite:///test_db.sqlite")


async def sql_session() -> AsyncSession:
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(sql_session)]


# items/models.py
class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str = Field(default=None, nullable=True)


# items/repository.py
class ItemRepository(SQLRepository[Item]):
    pass


# items/dependencies.py
def repository(session: SessionDep) -> ItemRepository:
    return ItemRepository(session)


# routes.py
class ItemController(ModelController, prefix="/item", tags=["Items"]):
    repository = Depends(repository)


# app.py
app = FastAPI()
app.include_router(ItemController.api_router)

if __name__ == '__main__':
    uvicorn.run(app)
```