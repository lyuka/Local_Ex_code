try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'One demo Project',
	'author': 'Ryuka',
	'verson': '0.1'
}

setup(**config)
