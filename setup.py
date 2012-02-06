from setuptools import setup

setup(
    name='django-staticpages',
    version='0.2.0',
    packages=['staticpages', 'staticpages.tests'],
    include_package_data=True,
    author='Gabriel Grant',
    author_email='g@briel.ca',
    license='LGPL',
    long_description=open('README').read(),
    url='http://github.org/gabrielgrant/django-staticpages/',
)

