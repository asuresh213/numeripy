from distutils.core import setup
setup(
  name = 'numeripy',
  packages = ['numeripy', 'numeripy.ODE_solvers', 'numeripy.matrix_methods'],
  version = '0.1.2',
  license='MIT',
  description = 'Python package for numerical analysis. Includes a variety of niche ode solvers and iterative matrix methods (typically encountered in a standard senior year course in numerical analysis)',   # Give a short description about your library
  author = 'Arun Suresh',
  author_email = 'ab251098@gmail.com',
  url = 'https://github.com/asuresh213/numeripy',
  download_url = 'https://github.com/asuresh213/numeripy/archive/v0.1.2.tar.gz',
  keywords = ['ODE Solvers', 'Numerical', 'Numerical Analysis', 'Optimization',
              'Matrix Methods', 'ODE', 'Differential Equations', 'Iterative matrix methods'],
  install_requires=[
          'numpy',
          'tabulate',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
