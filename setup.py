import setuptools

setuptools.setup(
    name='mac-comment',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
