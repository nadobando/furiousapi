## Class Based View Routing

The core of FuriousAPI routing is built on FastAPI's powerful router. Here's how you can define basic routes:

### Defining a Class Based View

```python
from http import HTTPMethod
from fastapi import FastAPI, Depends
from furiousapi.api import CBV
from furiousapi.api.controllers import mixins

from .dependencies import Dependency, dependency1

app = FastAPI()


# here you can add APIRouter parameters
class MyView(CBV, mixins.GetRouteMixin, mixins.PostRouteMixin, prefix="/some-prefix"):
    # configure the FastAPI route
    __route_config__ = {
        HTTPMethod.GET: {
            "response_model_exclude": {"some_field_to_exclude"}
        }

    }
    # you can add here FastAPI dependencies so they will be available in the function via `self.`
    dependency1 = Depends(dependency1)

    def get(self, another_dependency: Dependency) -> str:
        ...
        self.dependency1.do_foo()
        another_dependency.do_second_foo()
        return ""

    def post(self, another_dependency: Dependency) -> str:
        ...
        self.dependency1.do_foo()
        another_dependency.do_second_foo()
        return ""
```

### Adding `@action` to ClassBasedViews

```python
from http import HTTPMethod
from fastapi import Path
from furiousapi.api import CBV, action
from furiousapi.api.controllers import mixins
from .dependencies import Dependency


# here you can add APIRouter parameters
class MyView(CBV, mixins.GetRouteMixin, mixins.PostRouteMixin, prefix="/some-prefix"):

    @action("/an-action-path/{param1}", methods=[HTTPMethod.POST])
    def do_special_foo(self, another_dependency: Dependency, param1=Path()) -> str:
        ...

```

### Using existing `fastapi.APIRouter` in Class Based Views

this can be useful for nesting

```python
from fastapi import APIRouter

router = APIRouter()


class MyView(CBV, mixins.GetRouteMixin, mixins.PostRouteMixin):
    api_router = router

```