import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FrostGym",
    version="2024.04.18",
    author="-T.K.-",
    author_email="t_k_233@outlook.email",
    description="A gym environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ucb-bar/Retreat-Demo-Cartpole",
    project_urls={

    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8, <3.9",
)