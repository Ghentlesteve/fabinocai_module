from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="EDSA sample Python package",
    author="Steve Kwenev",
    author_email="<kwenevsteve@gmail.com>",  # Replace with actual email
    long_description=open("README.md").read(),
    install_requires=['numpy'],  # Example dependency
    url='https://github.com/Ghentlesteve/mypackage',  # Replace <username> with actual username
)