# Repository

The `FuriousAPI` embraces the repository pattern as a central design principle, abstracting the data access layer and
making it agnostic to the specific ORM/ODM used. This abstraction allows `ModelController` to be flexible and extensible
while providing a uniform interface for CRUD operations and more complex data manipulations.

## Repository Configuration

The `Repositoryonfig` class allows developers to define specific configurations that apply to data access, such as
fields to include or exclude in responses, sorting options, and pagination settings. These configurations are then
utilized by the `ModelController` to interact with the underlying data model in a consistent way.

```python
class RepositoryConfig:
    fields_include: ClassVar[Optional[Set[str]]] = None
    fields_exclude: ClassVar[Optional[Set[str]]] = None
    sort_include: ClassVar[Optional[Set[str]]] = None
    sort_exclude: ClassVar[Optional[Set[str]]] = None
    default_limit: ClassVar[int] = get_settings().pagination.default_size
    max_limit: ClassVar[int] = get_settings().pagination.max_size
    model_to_query: ClassVar[ModelDependency]
    filter_model: ClassVar[ModelMetaclass]
```

The settings within `RepositoryConfig` are used to construct the repository's behavior. This includes the fields and
sorting options that are allowed, the pagination defaults, and the models used for querying and filtering.

* **fields_include**: which fields will be included from the model and be able to be requested as the `fields`
* **fields_exclude**: which fields will be excluded from the model and be able to be requested as the `fields`
* **sort_include**: which fields will be sortable
* **sort_exclude**: which fields will be excluded from sortable enum
* **default_limit**: default pagination size
* **max_limit**: max pagination size
* **model_to_query**: how the model is processed as FastAPI dependency
* **filter_model**: currently converts all fields in a model to optional


```python
class ItemRepository(SQLRepository[Item]):
    class Config(RepositoryConfig):
        default_limit = 100
        sort_include = ("id", "name")
```

## Repository and ModelController Integration

The repository in `FuriousAPI` is tightly coupled with `ModelController`. The `ModelController` is dependent on a
repository to define how it operates. The meta-class `RepositoryMeta` dynamically attaches the model, sorting, fields,
and filtering configurations based on the repository's `Config` class.


- [SQLModel Integration](sqlmodel.md)
- [Beanie Integration](beanie.md)
- [PydangoORM (arangoDB) Integration](pydangorm.md)


