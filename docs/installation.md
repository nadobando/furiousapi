# Installation

Installing FuriousAPI is easy and can be customized depending on the extensions you plan to use. Follow these instructions to get started.

## Prerequisites

Before installing FuriousAPI, ensure that you have:

- Python 3.7 or higher
- A suitable virtual environment manager (like venv or conda)
- pip for installing Python packages

## Installing FuriousAPI

To install the core FuriousAPI package, run the following command in your virtual environment:

```bash
pip install furiousapi
```

To use FuriousAPI with SQLModel support, you can install it with the `sqlmodel` extra:

```bash
pip install "furiousapi[sqlmodel]"
```

Similarly, to install FuriousAPI with Beanie (ODM for MongoDB) support:

```bash
pip install "furiousapi[beanie]"
```

You can also install both extensions together:

```bash
pip install "furiousapi[sqlmodel,beanie]"
```

These commands will download and install FuriousAPI along with the selected extensions and their dependencies.

## Post-installation

After installation, you can create your first endpoint using FuriousAPI's class-based views (CBVs) with mixins to add methods as needed.

## Upgrading FuriousAPI

To upgrade FuriousAPI and its extensions to the latest versions, use the following command:

```bash
pip install --upgrade furiousapi
```

For extensions, replace `furiousapi` with the appropriate package name in the command above.

## Troubleshooting

If you encounter any issues during the installation:

- Verify that you have the correct version of Python installed.
- Ensure that your pip is up-to-date.
- Check any error messages during the installation process and look them up in the [Support](./support.md) section.

For more detailed instructions, including advanced configurations and environment setup, refer to the [Advanced Installation](./advanced_guide.md#advanced-installation) section in the Advanced Guide.
