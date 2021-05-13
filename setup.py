from setuptools import setup

setup(
    name="PySet",
    version="0.0.6",
    packages=["pyset"],
    entry_points={"console_scripts": ["pyset = pyset.__main__:main"]},
)
