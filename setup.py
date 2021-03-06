import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PollenTokyo",
    version="0.0.1",
    author="Yusuke Nakagomi",
    author_email="s1922021@stu.musashino-u.ac.jp",
    description="A package for pollen in Tokyo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s22anan/AI",
    project_urls={
        "Bug Tracker": "https://github.com/s22anan/AI",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['Scattered amount by pollen by Tokyo area'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'PollenTokyo = PollenTokyo:main'
        ]
    },
)
