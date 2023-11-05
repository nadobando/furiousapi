![logo-horizontal.png](images%2Flogo-horizontal.png)

Welcome to the official documentation for `FuriousAPI`.

**FastAPI** ❤️  **FuriousAPI**

## What is **FuriousAPI**?

Just as the name playfully suggests a connection to the high-octane **Fast & Furious** movie series 🤭

**FuriousAPI** aims to accelerate **[FastAPI](https://fastapi.tiangolo.com/)** development with additional features and
conveniences.

**FuriousAPI** is inspired by
the [Django REST Framework (DRF)](https://www.django-rest-framework.org/) and aims to bring the best practices and
design patterns of **DRF** into the asynchronous world of FastAPI.

## Features

- **Class Based Views**: Introduces class-based views with mixins to FastAPI, making your code more reusable and
  maintainable.
- **ModelController or ModelView**: Introduces model-based views to FastAPI, making the CRUD in just few lines of code
- **Cursor/Relay/Offset Pagination**: Introduces Pagination abstractions to be used by other extensions
- **Enhance Code Reuse and Standard**
- **Designed for Extensibility**: FuriousAPI provides a solid foundation, which can be extended with plugins
  like:
    - **`furiousapi-sqlmodel`** for SQL databases.
    - **`furiousapi-beanie`** for MongoDB.
- **Asynchronous Capabilities**: Integrates seamlessly with FastAPI to take full advantage of modern Python's async and
  await features.

## Philosophy

FuriousAPI is built with the following principles in mind:

- **Extensible**: Just like DRF, FuriousAPI offers multiple extension points so you can plug in your functionality or
  integrate with other libraries and frameworks.
- **Framework-agnostic**: FuriousAPI can be used with any Python DB framework, providing flexibility and freedom in
  choosing your tools.
- **Speed and Performance**: Embracing the async nature of FastAPI for non-blocking I/O operations.
- **Flexibility and Extensibility**: Offering a range of extensions to fit various data storage and processing
  requirements.
- **Expressive and Clear Syntax**: Aiming for an API design that is both intuitive and expressive, making your endpoints
  easy to read and write.
- **DRY Principles**: Reducing code repetition through mixins and generic classes, promoting reusability and
  maintainability.
- **Seamless Integration**: Designed to integrate smoothly with FastAPI's ecosystem, allowing for easy adoption within
  existing projects.
- **Type Safety and Validation**: Utilizes Pydantic models for robust data validation and schema definition, consistent
  with FastAPI's standards.
- **Ease of Use**: Developers can quickly create APIs with sensible defaults and powerful configuration options.
- **Extensibility**: Core components are designed to be extended or replaced to fit the needs of any project.
- **DRF's Design Patterns**: Brings DRF's mature design patterns into the FastAPI world, harmonizing Django's simplicity
  with FastAPI's performance.
- **DRF-Inspired Design**: Adopts the philosophies of DRF, focusing on modular, reusable components and clear, concise
  code.
- **Rich Ecosystem**: Leverage the power of the FastAPI ecosystem with enhanced capabilities provided by FuriousAPI
  extensions.

To begin using FuriousAPI, proceed to the [Installation](./installation.md) guide. To see how to build a fully-fledged
API with FuriousAPI, start with the [Tutorial](./tutorial.md).

