import setuptools
 
setuptools.setup(
    name="Qiime-top-OTU-search",
    version="0.1.8",
    author="midorikawa",
    author_email="ccm.penaei@gmail.com",
    description="qiimetophitsearch is my own python package",
    long_description="hogehoge",
    long_description_content_type="text/markdown",
    url="https://github.com/Sangoro053?tab=repositories",
    install_requires=['pandas'],
    packages=['q_search', 'qiimetophitsearch'],
    classifiers=[
        "Programming Language :: Python :: 3.7.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['q_search=q_search.call:q_search']
    }
)
