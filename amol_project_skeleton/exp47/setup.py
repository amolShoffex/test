try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Demo_Project',
    'author': 'AP_RJ',
    'url': 'Shoffex.com',
    'download_url': 'shoffex.com/downloads',
    'author_email': 'amol.shoffex@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['exp47'],
    'scripts': [],
    'name': 'Demo_Project'
}

setup(**config)

