from setuptools import setup

setup(
    name='python-qualtrics',
    version='0.0.1',
    url='https://github.com/tg2648/python-qualtrics',
    license='MIT',
    author='tg2648',
    install_requires=['requests'],
    description='Python client for the Qualtrics API',
    packages=['qualtrics', 'qualtrics.components'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries',
    ],
)
