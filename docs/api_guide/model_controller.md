## ModelController

FuriousAPI's `ModelController` is a powerful abstraction built on top of the `CBV` (Class-Based View), designed to
streamline interactions with data models for CRUD operations and beyond, while minimizing the need for repetitive
boilerplate code. It inherits all the benefits of `CBV` and extends them with model-specific capabilities.

### Defining a ModelController

A `ModelController` is defined by extending the `ModelController` base class, which itself inherits from `CBV`. This
setup provides a structured approach to building API endpoints, emphasizing reuse and maintainability. Here's how you
can define a `ModelController`:

#### Requirements
in order to be able to use the `ModelController` you need to define the `repository` **FastAPI** dependency

```python
from fastapi import Depends
from furiousapi.api import ModelController
from .repository import ItemRepository


# Define the ModelController
class ItemController(ModelController):
    # as the CBV, dependencies can be added
    repository = Depends(ItemRepository)

    # Optionally, override default methods or add new endpoints
    # ...
```

By inheriting from `CBV`, `ModelController` allows for the organization of request handling logic in a class-based
structure, enabling more complex compositions and reuse of common functionality.

### Customizing Endpoints with `@action`

The `ModelController` can be further customized with the `@action` decorator to define custom actions, adding an extra
layer of functionality to the endpoints:

```python
from http import HTTPMethod
from fastapi import Depends
from furiousapi.api import ModelController, action
from .repository import ItemRepository


class ItemController(ModelController):
    # ...

    @action("/sold", methods=[HTTPMethod.PATCH])
    async def mark_as_sold(self, id_: int):
        # Implement custom logic to mark an item as sold
        pass
```

The `@action` decorator enhances the expressiveness of the `ModelController`, giving you the ability to specify actions
on both detail and list routes and to respond to various HTTP methods.

### Integrating with FastAPI's Routing

`ModelController` is designed to integrate smoothly with FastAPI's routing, allowing you to easily include its routes in
your FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()
item_controller = ItemController()

# Include the controller's routes into the FastAPI app
app.include_router(item_controller.api_router)
```

By integrating `ModelController` into your FastAPI application, you expose a suite of endpoints that encapsulate CRUD
operations and any additional actions you've defined, following RESTful principles and best practices.
