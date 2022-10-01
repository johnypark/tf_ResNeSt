import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tf_ResNeSt", # Replace with your own username
    version="1.0",
    author="QiaoranC",
    author_email="QiaoranC",
    description="TF-ResNest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QiaoranC/tf_ResNeSt_RegNet_model",
    packages=setuptools.find_packages(),
    install_requires = ['tensorflow'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

