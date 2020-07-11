from setuptools import setup, find_packages

setup(
    name='intotherain',
    version='0.0.2',
    description='Basic Calculator',
    author='time_to_bye',
    author_email='secret@secret.com',
    url='https://github.com/timetobye/Make_pypi_practice',
    packages=find_packages(exclude=['docs', 'test.py']),
    install_requires=[],
    keywords=['practice', 'temp_practice'],
    python_requires='>=3'
)