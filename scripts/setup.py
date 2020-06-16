import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pandashape",
    version="0.0.4",
    author="Ben Stein",
    author_email="ben.s.stein@gmail.com",
    description="A package designed to simplify data preprocessing for use with Pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jammerware/pandashape.git",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
