import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='enos-mqtt-sdk-python',
    version='0.1.0',
    author='EnvisionIot',
    author_email='EnvisionIot',
    description='EnOS MQTT SDK for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages(),
    install_requires=[
        'futures; python_version == "2.7"',
        'paho-mqtt >= 1.4.0',
        'certifi'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
