  
from setuptools import setup, find_packages

setup(
    name="trial",
    version="0.1.0",
    description="",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Deyviss Jesus Oroya Villalta",
    author_email="djoroya@gmail.com",
    url="https://github.com/djoroya/trial",
    packages=find_packages(),  # Encuentra  los paquetes en la carpeta src
    project_urls={
        "Source Code": "https://github.com/djoroya/trial",
        "Bug Tracker": "https://github.com/djoroya/trial/issues",
    },
    # from requeriments.txt
    install_requires=open('requirements.txt').read().splitlines(),
    python_requires='>=3.6',  #   de Python requerida
    classifiers=[  # Clasificadores que ayudan a otros desarrolladores a encontrar tu proyecto
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Tipo de licencia
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={
    },
)
  