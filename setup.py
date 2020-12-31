from setuptools import setup, find_packages


install_requires = open("requirements.txt").readlines()
console_scripts = [
    'meter-producer = pvs.meter:main',
    'simulator-consumer = pvs.simulator:main'
]

options = {}

setup(name="pvs",
      use_scm_version=True,
      setup_requires=["setuptools_scm"],
      description="PV Simulator",
      author="Denis Guzeyev",
      author_email="denis.guzeyev@gmail.com",
      platforms=["linux"],
      zip_safe=True,
      packages=find_packages(),
      py_modules=[],
      data_files=[
          "requirements.txt",
      ],
      include_package_data=True,
      install_requires=install_requires,
      extras_require = {},
      entry_points = {
          "console_scripts": console_scripts,
      },
      **options)
