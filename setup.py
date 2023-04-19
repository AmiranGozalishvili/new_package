from setuptools import setup

setup(name="package_1",
        version="1.0",
        packages=['.package_1'],
        options={"bdist_wheel":{"universal":True}}
    )

