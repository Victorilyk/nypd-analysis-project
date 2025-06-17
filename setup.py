from setuptools import setup, find_packages

setup(
    name='analysis_lib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'run-analysis=analysis_lib.__main__:main',
        ],
    },
    author='Viktor Ilyk',
    description='Package for NYPD Final Assignment analysis',
)
