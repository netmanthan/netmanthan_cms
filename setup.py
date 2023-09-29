from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in netmanthan_cms/__init__.py
from netmanthan_cms import __version__ as version

setup(
	name="netmanthan_cms",
	version=version,
	description="netmanthan CMS",
	author="netmanthan",
	author_email="info@netmanthan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
