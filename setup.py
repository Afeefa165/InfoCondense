import setuptools

with open("Readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__  = "0.0.0"

REPO_NAME = "InfoCondense"
AUTHOR_USER_NAME = "afeefa165"
SRC_REPO = "InfoCondense"
AUTHOR_EMAIL = "afeefahh165@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author =AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python package for NLP App",
    long_description_content_type="text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages= setuptools.find_packages(where="src"),
    package_dir = {"":"src"}
)