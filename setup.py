from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='rpn',
      version='1.0',
      description='Reverse Polish Notation calculator.',
      long_description=readme(),
      keywords='math calculator rpn arithmetic',
      url='https://github.com/dustinrohde/python-rpn',
      author='Dustin Rohde',
      author_email='xdrohdex@gmail.com',
      license='MIT',
      packages=['rpn'],
      scripts=['bin/rpn'],
      zip_safe=False)
