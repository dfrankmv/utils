from setuptools import setup, find_packages

# --------------------- #
# utils/utils structure #
# --------------------- #

setup(
    name="utils",
    version='0.1.0',
    packages=find_packages(),
    package_dir={"utils":"utils"},
    install_requires=[
        "pytest",
        "pyzmq",
        "requests",
        "websocket-client",
    ],
)