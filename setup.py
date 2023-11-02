
from setuptools import setup, find_packages

name = "FuriousAPI"
lower_name = name.lower()
furiousapi = f'https://github.com/nadobando/{lower_name}'
map_={
    'sqlmodel': f'{lower_name}-sqlmodel @ git+{furiousapi}-sqlmodel.git@main#egg={lower_name}-sqlmodel',
    'beanie': f'{lower_name}-beanie @ git+{furiousapi}-beanie.git@main#egg={lower_name}-beanie',
}

setup(
    name=name,
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        f'{lower_name}-core @ git+{furiousapi}-core.git@main#egg={lower_name}-core',
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
