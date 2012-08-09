import multiprocessing, logging
import sys
from setuptools import setup, find_packages

version = '0.0.1' 

install_requires =[ 
	"flask", 
	"sqlalchemy", 
	"pymysql"
]

setup(name="eVote", 
		version=version, 
		description="CSH eVote", 
		long_description="Cmoputer Science House Electronic Vote System", 
		classifiers = [  
			"Development Status :: 1 - Planning", 
			"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"], 
		keywords="eVote CSH", 
		author="Will Dignazio", 
		url="http://github.com/WillDignazio/eVote", 
		license="GPLv3+", 
		packages=find_packages(), 
		include_package_data=True, 
		zip_safe=False, 
		install_requires=install_requires, 
)

