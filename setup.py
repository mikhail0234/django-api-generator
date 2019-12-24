import os
from setuptools import setup, find_packages


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='api-generator',
    version='1.4',

    description='Generate api for django app',
    license='MIT',

    packages=['api_generator', 'api_generator.templates', 'api_generator.management',
              'api_generator.management.commands'],
    include_package_data=True,
    install_requires=['Django>=2.0'],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
