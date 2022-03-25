import setuptools

setuptools.setup(
    name="mpc_training",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=['flask', 'pytest', 'python-dotenv', 'numpy']
)
