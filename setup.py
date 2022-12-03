from setuptools import setup, find_packages
from lightning_utils import __version__

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="lightning_utils",
    packages=find_packages(include=["lighning_utils"]),  # add other exclusions in future
    version=__version__,
    license="MIT",
    description="A collection of utilities for PyTorch Lightning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vahid Zehtab",
    author_email="vahid@zehtab.me",
    url="https://github.com/vahidzee/lightning_utils",
    keywords=["artificial intelligence", "pytorch lightning", "objective functions", "regularization"],
    install_requires=["torch>=1.9", "lightning", "dycode==0.0.2"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)