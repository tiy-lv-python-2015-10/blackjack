import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flynn-blackjack",
    version="0.0.1",
    description="Basic Terminal Blackjack",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/peteralfredoflynn/blackjack",
    author="Peter Flynn",
    author_email="peterflynndev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["blackjack"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "realpython=blackjack.__main__:main",
        ]
    },
)
