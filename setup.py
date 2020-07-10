from setuptools import setup, find_packages

setup(
    name='intotherain',
    version='0.0.1',
    description='Basic Calculator',
    author='time_to_bye',
    author_email='secret@secret.com',
    url='https://github.com/timetobye/Make_pypi_practice',
    packages = find_packages(),
    install_requires=[
        'numpy==1.19.0',
        'pandas==1.0.5',
        'python-dateutil==2.8.1',
        'pytz==2020.1',
        'six==1.15.0'
    ],
    keywords=['practice', 'temp_practice'],
    python_requires='>=3'
)