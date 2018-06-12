import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./umdcli/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='umdcli',
    version=version,
    description="""The Universal Mega Dumper (UMD) is a game catridge read/writer project designed around a Teensy++ microcontroller. The universality comes from the UMD's ability to support many different types of catridge connectors by having general purpose 16 bit data and 24 bit address paths along with a dozen control signals - all of which can be customized for each game cartridge mode.""",
    long_description=long_description,
    author='René Richard',
    author_email='umd@db-electronics.ca',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=find_packages(
        exclude=[
            'docs', 'tests',
            'windows', 'macOS', 'linux',
            'iOS', 'android',
            'django'
        ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    install_requires=[
        'pyserial',
    ],
    options={
        'app': {
            'formal_name': 'Universal Mega Dumper',
            'bundle': 'ca.db-electronics'
        },
    },
    entry_points={
        'console_scripts': [
            'umd = umdcli.__main__:main'
        ]
    },
)
