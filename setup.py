from setuptools import setup, find_packages

# Read requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name='cryptograde',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    url='https://github.com/ThomasPluck/cryptograde',
    author='Thomas Pluck',
    author_email='thomaspluck95@gmail.com',
    description='A set of Python utilities for local assignment grading in Jupyter Notebooks',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
