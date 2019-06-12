from setuptools import setup

setup(
    name='pys-viacep',
    version='0.0.1',
    description='Consulta simplificada de enderecos pelo CEP no webservice VIACEP',
    url='https://github.com/rfschubert/pys-viacep',
    author='Raphael Schubert',
    author_email='rfswdp@gmail.com',
    license='MIT',
    packages=['pys-viacep'],
    keywords=['python viacep', 'python3', 'viacep', 'schubert'],
    install_requires=[
        'requests'
    ],
    zip_safe=False
)