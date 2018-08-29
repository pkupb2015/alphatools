from setuptools import setup, find_packages

setup(
    name='alphatools',
    version='0.11',
    description='Quant finance resarch tools',
    author='Jonathan Larkin',
    author_email='jonathan.r.larkin@gmail.com',
    url = "https://github.com/marketneutral/alphatools",
    download_url = "https://github.com/marketneutral/alphatools/archive/0.11.tar.gz",
    packages=find_packages(),
    install_requires=[
        'zipline',
        'alphalens',
        'blaze',
        'ipykernel'
    ]
)
