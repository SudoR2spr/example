from setuptools import setup

setup(
    name='encoded',  # The name of the package
    version='0.1',
    py_modules=['encoded'],
    install_requires=[
        'requests',  # Your other dependencies
        'Flask',
    ],
)
