from setuptools import setup, find_packages

setup(
    name="kalki",
    version="0.1",
    description="Kalki is a library to create dynamic CSS",
    author="Biswajit Bimoli",
    packages=['kalki'],
    author_email='biswajitbimoli@gmail.com',
    url='https://github.com/biswajitbimoli/kalki',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    # package_dir={'': '/'},
    # packages=find_packages(include=['kalki', 'kalki.*', 'bin']),
    # entry_points={
    #     'console_scripts': [
    #         'kalki = kalki:main'],
    # },
    include_package_data=True,
)