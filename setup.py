import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TestRepo",
    version="0.0.2",
    author="Richard Brenick",
    author_email="RichardBrenick@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rBrenick/TestRepo",
    packages=setuptools.find_packages(),
    package_data={'': ['*.*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    install_requires=[
    "Qt.py",
    "p4python",
    ]
)