#!/usr/bin/env python3
# setup.py

from setuptools import setup

setup(
	name='GHOffline',
	version ='1.0',
	description = 'Check offline site in a repository of Github',
	long_description = '''
	GHOffline
	===========
	Check offline site in a repository of Github

	How to use
	===============
	$> ghoffline your_username your_password user/repo

	Output in text (off_<user_repo>.txt)

	Very simple :)
	''',
	author = 'Tiago Danin',
	author_email = 'TiagoDanin@outlook.com',
	license = 'GPLv3',
	url = 'https://TiagoDanin.github.io/ghoffline/',
	scripts = ['ghoffline'],
	install_requires= [
		'pygithub',
		'regex',
		'requests'
	],
	classifiers = [
		'Natural Language :: English',
		'Operating System :: MacOS',
		'Operating System :: Unix',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Utilities'
	],
	keywords = 'http https offline validation github repository repo'
)
