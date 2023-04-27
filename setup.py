from setuptools import setup

setup(name="package1",
        version="1.0",
        packages=['.package1'],
        options={"bdist_wheel":{"universal":True}}
    )

