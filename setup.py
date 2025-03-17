from setuptools import setup, find_packages

setup(
    name= "scanner",
    version="1.0.0",
    author="Gunavardhan Naidu",
    packages=find_packages(),
     install_requires=[
        "python-whois==0.9.5",
        "requests==2.32.3",
        "scapy==2.6.1",
        "typing-extensions==4.12.2",
        "urllib3==2.3.0",
        "vt-py==0.19.0",
        "yarl==1.18.3",
        "ipinfo==5.1.1"
    ],
    entry_points={
        "console_scripts": [
            "scanner=main:main",
        ],
    },
)