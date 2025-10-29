from setuptools import setup, find_packages

setup(
    name="utils",
    version='0.1.0',
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_dir={"utils":"utils"},
    install_requires=[
        "pytest",
        "pyzmq",
        "requests",
        "websocket-client",
    ],
)