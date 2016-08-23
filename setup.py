from setuptools import setup, find_packages


VERSION = '1.0.0.dev0'


setup(
    name='psu.oit.wdt.ecoroofs',
    version=VERSION,
    description='EcoRoofs',
    author='PSU - OIT - WDT',
    author_email='webteam@pdx.edu',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=1.10.1',
        'django-arcutils>=2.11.1',
        'django-haystack>=2.4.1,<2.5',
        'django-local-settings>=1.0b1',
        'django-pgcli>=0.0.2',
        'djangorestframework>=3.4.1',
        'elasticsearch>=1.9.0,<2.0',
        'psycopg2>=2.6.2',
        'pytz>=2016.6.1',
        'psu.oit.arc.tasks',
    ],
    extras_require={
        'dev': [
            'flake8',
        ]
    },
)
