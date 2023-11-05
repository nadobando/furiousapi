# Beanie Integration with FuriousAPI

[Beanie](https://beanie-odm.dev/) is an asynchronous ODM (Object-Document Mapper) for MongoDB, built on top of Motor. In `FuriousAPI`,
the `furiousapi-beanie` extension integrates Beanie to provide a seamless experience when working with MongoDB.

## Repository Pattern with Beanie

The repository pattern in `FuriousAPI` abstracts away the data access layer. With the `furiousapi-beanie` extension,
this pattern is implemented for MongoDB using Beanie. This allows for a consistent CRUD interface and query
capabilities, abstracting away the specifics of MongoDB access.

## Setting up a Beanie Repository

To set up a Beanie repository in `FuriousAPI`, you need to define a model using Beanie's `Document` class and then
create a repository class that extends `BeanieRepository`. The repository class will handle the data operations for the
model.

```python
from typing import Optional

from beanie import Document, init_beanie
from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from furiousapi.beanie import MongoRepository
from furiousapi.api import ModelController


# Define your Beanie document
class Item(Document):
    name: str
    description: Optional[str] = None


# Extend MongoRepository to create your repository class
class ItemRepository(MongoRepository[Item]):
    pass


# Use the ItemRepository with a ModelController
class ItemController(ModelController):
    repository = Depends(ItemRepository)


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient()
    database = AsyncIOMotorDatabase(client, "app")
    await init_beanie(database, document_models=[Item])


app.include_router(Item)
```

## Integrating with ModelController

Once you have your Beanie repository set up, you can integrate it with `ModelController` to provide a fully functional
API interface for your MongoDB documents.

## Async Operations

All operations in the Beanie repository are asynchronous, leveraging Python's async and await features for non-blocking
I/O operations with MongoDB.

## Conclusion

The `furiousapi-beanie` extension offers a powerful way to integrate MongoDB with your `FuriousAPI` projects, harnessing
the repository pattern for clean, maintainable code that abstracts away database access.

For more detailed examples and advanced configurations, refer to the `Beanie` documentation and the `furiousapi-beanie`
extension guide.
