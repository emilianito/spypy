from setuptools import setup

setup(
    name='spypy',
    packages=['spypy'],
    version='0.1',
    description='A lib for get profiling your code',
    author='Emiliano Nunez',
    author_email='nunez.emiliano@gmail.com',
    url='https://github.com/emilianito/spypy',
    keywords=['profiling', 'tracer'],
    license='GPLv3',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Debuggers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
