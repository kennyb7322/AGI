"""
AGI Framework Setup
Copyright (c) 2026 kennyb7322
Licensed under the MIT License
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agi-framework",
    version="1.0.0",
    author="kennyb7322",
    description="A comprehensive framework for building Artificial Generative Intelligence systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kennyb7322/AGI",
    project_urls={
        "Bug Tracker": "https://github.com/kennyb7322/AGI/issues",
        "Documentation": "https://github.com/kennyb7322/AGI/tree/main/docs",
        "Source Code": "https://github.com/kennyb7322/AGI",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    keywords="artificial-intelligence generative-ai machine-learning deep-learning neural-networks nlp text-generation",
    license="MIT",
)
