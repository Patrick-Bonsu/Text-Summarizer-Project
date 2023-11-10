import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


__version__="0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME ="Patrick-Bonsu"
SRC_REPO= "textSummarizer"
AUTHOR_EMAIL = "bonsuyeboahmurphy@gmail.com"



setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Patrick-Bonsu/Text-Summarizer-Project",
    project_urls={
        "Bug Tracker": f"https://github.com/Patrick-Bonsu/Text-Summarizer-Project/issues",    
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)    