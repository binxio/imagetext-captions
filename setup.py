from setuptools import setup, find_packages

setup(
    name="ImageTextCaptions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.26.0",
        "google-auth>=1.35.0"
    ],
    author="Dennis Vink",
    author_email="dennis.vink@xebia.com",
    description="A module to generate captions for images using Google AI's Vertex AI Platform.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/binxio/imagetext-captions",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
