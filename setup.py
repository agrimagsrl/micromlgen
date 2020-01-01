from distutils.core import setup
setup(
  name = 'micromlgen',
  packages = ['micromlgen'],
  version = '0.8',
  license='MIT',
  description = 'Generate C code for microcontrollers from Python\'s sklearn classifiers',
  author = 'Simone Salerno',
  author_email = 'web@agrimag.it',
  url = 'https://github.com/agrimagsrl/micromlgen',
  download_url = 'https://github.com/agrimagsrl/micromlgen/archive/v_08.tar.gz',
  keywords = ['ML', 'microcontrollers', 'sklearn', 'machine learning'],
  install_requires=[
    'jinja2',
  ],
  package_data= {
    'micromlgen': ['templates/*.jinja']
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Code Generators',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)