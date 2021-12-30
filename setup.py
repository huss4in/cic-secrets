import os
import setuptools

projectURL = ''

with open(f"{os.path.dirname(os.path.realpath(__file__))}/README.md", 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='cic-secrets',
    version='0.1.0',

    author='huss4in',
    author_email='huss4in.sultan@gmail.com',

    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url=projectURL,
    project_urls={
        'Bug Tracker': f"{projectURL}/issues",
    },

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Topic :: Security :: Cryptography"
    ],

    python_requires='>=3.9',

    install_requires=["requests"],

    package_dir={'': 'src'},

    packages=setuptools.find_packages(where='src'),
)
