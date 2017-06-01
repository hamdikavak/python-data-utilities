from setuptools import setup

setup(
    name='data_utils',
    version='0.0.1',
    description='Data utilities and wrappers for academic data science projects.',
    author='Hamdi Kavak',
    author_email='hkava001@odu.edu',
    url='https://github.com/hamdikavak/python-data-utilities',
    license='MIT',
    keywords='data science, utility, wrapper',
    scripts = ['bin/pgsql2csv.py'],
    install_requires=['psycopg2==2.7.1',
                      'numpy==1.12.1',
                      'matplotlib==2.0.1',
                      'pandas==0.20.1']
    )