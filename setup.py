from setuptools import setup, find_packages

# metadata
# used when someone installs my package 

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: End Users/Desktop',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3.8'
]

setup(
    name='clac',
    version=1.0,
    author='Rubem Vasconcelos Pacelli',
    author_email='rubem.engenharia@gmail.com',
    url='https://github.com/tapyu/clac',
    description='RPA to automatically create language cards on Anki with audio/examples from Collins.',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    license='MIT',
    packages=find_packages(),
    keywords=['Anki', 'RPA', 'Language cards'],
    install_requires=['requires'],
    classifiers=classifiers
)