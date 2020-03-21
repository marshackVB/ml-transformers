import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "mlc-ml-transformers",
    version = "0.0.1",
    author = "Marshall Carter",
    author_email = "carter.marshall@gmail.com",
    desciption = "custom scikit-learn transfomers",
    long_description = long_description,
    long_destricption_content_type = "text/markdown",
    url = "https://github.com/marshackVB/tranformers",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires = ["pandas", "sckikit-learn"],
    python_requires =  ">=3.6"
)