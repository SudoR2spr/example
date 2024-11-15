from setuptools import setup

setup(
    name='encoded_op',  # The name of the package
    version='0.1',
    py_modules=['encoded_op'],
    install_requires=[
        'requests',  # Your other dependencies
        'Flask',
    ],
)
