import setuptools

setuptools.setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    packages=setuptools.find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'pytest-cov',
            'bandit',
            'black'
        ]
    }
)
