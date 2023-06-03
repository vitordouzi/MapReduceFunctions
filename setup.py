from setuptools import setup, find_packages

setup(
    name='MRF',
    version='1.0.0',
    author='Vitor Mangaravite',
    author_email='vitordouzi@gmail.com',
    description='A package with simple-pure-python Map-Reduce Functions.',
    long_description='A package that provides map-reduce functions for data processing.',
    long_description_content_type='text/markdown',
    url='https://github.com/vitordouzi/MapReduceFunctions',
    packages=find_packages(exclude=['tests']),  # Exclude 'tests' directory from package inclusion
    python_requires='>=3.6',  # Specify the minimum Python version required
    install_requires=[],  # Add package dependencies if any
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
