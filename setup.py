import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chest_Cancer_Classification_using_MLFlow_DVC"
AUTHOR_USER_NAME = "AliTheAnalyst01"
SRC_REPO = "CNNClassifier"  # Fixed typo from 'cmnClassifier' to 'cnnClassifier'
AUTHOR_EMAIL = "faizanzaidy78@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fixed parameter name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "tensorflow>=2.6.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
    ]
)