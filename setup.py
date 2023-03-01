from setuptools import setup
"""
source: https://www.geeksforgeeks.org/what-is-setup-py-in-python/
"""

"""setup
"""
setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='John Doe',
    author_email='jdoe@example.com',
    packages=['my_package'],
    install_requires=[
        'numpy',
        'pandas',
    ],
)
