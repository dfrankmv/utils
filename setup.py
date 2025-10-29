from setuptools import setup, find_packages

# --------------------- #
# utils/utils structure #
# --------------------- #

# setup(
#     name="utils",
#     version='0.1.0',
#     packages=find_packages(exclude=["tests", "tests.*"]),
#     package_dir={"utils":"utils"},
#     install_requires=[
#         "pytest",
#         "pyzmq",
#         "requests",
#         "websocket-client",
#     ],
# )


# ---------------------- #
# utils/<code> structure #
# ---------------------- #

setup(
    name="utils",
    version='0.1.0',
    packages=["utils"],
    package_dir={"utils":"."},
    # packages=find_packages(include=["utils"], exclude=["utils.*"], ),
    install_requires=[
        "pytest",
        "pyzmq",
        "requests",
        "websocket-client",
    ],
)