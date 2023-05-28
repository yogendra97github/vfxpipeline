import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vfxpipe",
    version="0.0.1",
    author="Yogendra Singh",
    author_email="yogendrasingh.hqvfx@gmail.com",
    description="A studio Pipeline for 3d animation and VFX studio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yogendra97github/GitDemoProjectV1",
    project_urls={
        "Bug Tracker": "https://github.com/yogendra97github/GitDemoProjectV1/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9"
)
