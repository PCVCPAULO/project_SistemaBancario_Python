from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read() 

setup(
    name="sistema_bancario_pcvcpaulo",
    version="0.0.2",
    author="PCVCPAULO",
    author_email="pcvcpaulo@gmail.com",
    description="Simula um sistema bancário",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PCVCPAULO/project_SistemaBancario_Python",
    packages=find_packages(),
    python_requires='>=3.8',
)
