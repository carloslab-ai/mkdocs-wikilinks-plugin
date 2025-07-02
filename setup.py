from setuptools import setup, find_packages

description = "A mkdocs plugin that makes linking to other documents easy."
long_description = description

version="0.1.1"

with open("README.md", "r") as f:
    long_description = f.read()
with open("requirements.txt", "r") as f:
    required=f.read().splitlines()
setup(
    name="mkdocs-wikilinks-plugin",
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs, wikilinks, ezlinks, obsidian, roam",
    url="https://github.com/carloslab-ai/mkdocs-wikilinks-plugin",
    author="Carlos",
    author_email="carlos@carloslab-ai.com",
    license="MIT",
    python_requires=">=3.6",
    install_requires=required,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(exclude=["test.*"]),
    entry_points={
        "mkdocs.plugins": ["ezlinks = mkdocs_ezlinks_plugin.plugin:EzLinksPlugin"]
    },
)
