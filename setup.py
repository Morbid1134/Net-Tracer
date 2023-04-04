from setuptools import setup

setup(
    name='nettracer',
    version='0.1.0',
    description='A simple port scanner',
    py_modules=['nettracer'],
    install_requires=[
        'nmap==0.7.1',
        'pyfiglet==0.7.5'
    ],
    entry_points='''
        [console_scripts]
        nettracer=nettracer:main
    '''
)
