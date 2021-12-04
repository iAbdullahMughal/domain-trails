import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
version = "1.0.0"
packages = [
    "domaintrails",
    "domaintrails.core",
    "domaintrails.core.parser",
    "domaintrails.core.recon",

]
package_data = {
    'domaintrails': [
        'README.html',
        'LICENSE.txt',
    ]
}

entry_points = {
    'console_scripts': [
        'domaintrails=domaintrails.portal:main',
    ],
}

setuptools.setup(
    name="domain-trails",
    version=version,
    author="Muhammad Abdullah",
    author_email="iamabdullahmughal@gmail.com",
    description="Domain trails is open source intelligence gathering tool. This tool collect information "
                "related to domain. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iAbdullahMughal/domain-trails",
    project_urls={
        "Bug Tracker": "https://github.com/iAbdullahMughal/domain-trails/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=packages,
    package_data=package_data,
    entry_points=entry_points,
    python_requires=">=3.6",
)
