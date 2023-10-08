from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="civitai",
    version="0.1",
    author="Lorg0n",
    author_email="lorgon.kv@gmail.com",
    description="The library allow you to generate images using the built-in civitai capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "requests",
    ]
)
