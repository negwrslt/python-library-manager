from setuptools import setup, find_packages

setup(
    name="mylibrary",
    version="0.2.0",
    description="A modular Python package and CLI for cataloging and managing books",
    author="Negar Soltaniani",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "library-manager=main:menu",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
