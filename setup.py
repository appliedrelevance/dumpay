from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dumpay/__init__.py
from dumpay import __version__ as version

setup(
	name="dumpay",
	version=version,
	description="Dummy Payment Gateway for testing and development ecommerce sites.",
	author="Applied Relevance",
	author_email="geveritt@appliedrelevance.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
