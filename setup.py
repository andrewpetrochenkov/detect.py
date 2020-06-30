import setuptools

setuptools.setup(
    name='detect',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
