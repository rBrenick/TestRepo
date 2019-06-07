import setuptools
from setuptools.command.install import install

with open("README.md", "r") as fh:
    long_description = fh.read()


print("#"*50)
print("#"*50)
print("SETUP.py extra things")
print("#"*50)
print("#"*50)


class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        print "Hello, developer, how are you? :)"
        install.run(self)
    

setuptools.setup(
    name="TestRepo",
    version="0.0.3",
    author="Richard Brenick",
    author_email="RichardBrenick@gmail.com",
    description="A small example package",
    url="https://github.com/rBrenick/TestRepo",
    cmdclass={
        'install': CustomInstallCommand,
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
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

