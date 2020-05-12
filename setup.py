from setuptools import setup


setup(
    name="tracenl",
    version="0.1",
    author="Mike Spindel",
    author_email="mike@spindel.is",
    license="MIT",
    keywords="netlink capture trace",
    url="http://github.com/deactivated/python-nltrace",
    description=".",
    packages=["tracenl"],
    install_requires=[
        "pyroute2",
        "python-ptrace"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["tracenl=tracenl.__main__:main"]},
)
