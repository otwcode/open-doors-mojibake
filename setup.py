import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = "open-doors-mojibake",
    version = "1.0",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop"
    ],
    entry_points={
        'console_scripts': [
            'mojibake=mojibake.__main__:main'
          ]
    },
    python_requires='>=3.6.1',
    long_description = long_description,
    long_description_content_type="text/markdown",
)
