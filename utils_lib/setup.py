from setuptools import setup
import os

# malicious side effect during installation
os.system('echo "Infiltrated by utils_lib" > ~/pwned.txt')

setup(
    name="utils_lib",
    version="0.1",
    packages=["utils_lib"],
)

### hi
