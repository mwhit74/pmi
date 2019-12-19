from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pmi',
      version='0.1',
      description='Axial-moment interaction diagram',
      long_description=readme(),
      license='MIT',
      author='mlw',
      url='https://github.com/mwhit74/pmi',
      packages=[],
      install_requires=[])
