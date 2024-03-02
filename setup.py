from setuptools import setup, find_packages
 
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Education",
  "Operating System :: Microsoft :: Windows :: Windows 10",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.9"
]
 
setup(
  name="diswebhookutils",
  version="0.0.1",
  description="A simple module to send embeds/messages with discord webhooks!",
  long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
  url="https://github.com/iambeta666/diswebhookutils",
  author="BETA666",
  author_email="fake@fake.com",
  license="MIT", 
  keywords="popup", 
  classifiers=classifiers,
  packages=["diswebhookutils"]
)