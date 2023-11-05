from setuptools import setup, find_packages

name = "FuriousAPI"
lower_name = name.lower()
core_version = "0.1.0"
map_ = {
    'sqlmodel': f'{lower_name}-sqlmodel>={core_version}',
    'beanie': f'{lower_name}-beanie>={core_version}',
}

setup(
    name=name,
    version=core_version,
    # packages=find_packages(),
    install_requires=[
        f'{lower_name}-core>={core_version}',
    ],

    extras_require={
        'sqlmodel': [map_["sqlmodel"]],
        'beanie': [map_["beanie"], ],
        'all': [
            map_["sqlmodel"],
            map_["beanie"],
        ],
    }
)
