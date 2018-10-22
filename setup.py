from setuptools import setup, find_packages


setup(
    name='quizscrambler',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
            [console_scripts]
            scramblequiz=quizscrambler.main:scramblequiz
        ''',
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.yaml', '*.md']
    },
    license='Apache 2.0',
    author='J Sebastian Paez',
    author_email='jpaezpae@gmail.com',
    description='given a quiz in YAML format, returns multiple scrambled versions of it'
)
