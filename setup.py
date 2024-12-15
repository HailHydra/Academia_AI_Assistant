from setuptools import find_packages,setup

setup(
    name='Mentor Bot',
    version='1.1.1',
    author='Varun',
    author_email='darklususnaturae@gmail.com',
    install_requires=[
        'openai',
        'flask',
        'setuptools'
    ],
    packages=find_packages()
)