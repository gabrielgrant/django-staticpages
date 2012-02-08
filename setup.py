from setuptools import setup

setup(
    name='django-staticpages',
    version='0.2.3',
    packages=['staticpages', 'staticpages.tests', 'staticpages.templatetags'],
    include_package_data=True,
    author='Gabriel Grant',
    author_email='g@briel.ca',
    license='LGPL',
    long_description=open('README').read(),
    url='http://github.org/gabrielgrant/django-staticpages/',
)

