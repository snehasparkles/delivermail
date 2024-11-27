from setuptools import setup, find_packages

setup(
    name="delivermail", 
    version="0.1.0",
    author="Sneha", 
    author_email="m.sneha161102@gmail.com",  
    description="A simple Python package for sending emails via SMTP",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/snehasparkles/delivermail",  
    packages=find_packages(),
    py_modules=["delivermail"], 
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
