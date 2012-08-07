import os
from setuptools import setup, find_packages
version = '0.1.0'
README = os.path.join(os.path.dirname(__file__), 'README')
long_description = open(README).read()
setup(name='exif-py',
      version=version,
      description=("Library for importing exif data from uploaded images.Originally written by Gene Cash / Thierry Bousch. Converted to pip setup."),
      long_description=long_description,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      keywords='exif image',
      author='Llewellyn Hinkes-Jones',
      author_email='ortsed@gmail.com',
      url='https://github.com/ortsed/exif-py',
      download_url='https://github.com/ortsed/exif-py/zipball/master',
      license='BSD',
      packages=find_packages(),
      )
