from setuptools import setup, find_packages

setup(
    name="text_adventure",
    version="0.0.1",
    description="Simple text adventure game",
    author="KlingonDragon",
    url="https://github.com/KlingonDragon/text-adventure",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={"console_scripts": ["start-text-adventure = text_adventure.__main__:start"]},
)
