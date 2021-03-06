import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.2'
PACKAGE_NAME = 'random_spanish' #Debe coincidir con el nombre de la carpeta 
AUTHOR = '@fcoterroba.com' #Modificar con vuestros datos
AUTHOR_EMAIL = 'fcoterroba@gmail.com' #Modificar con vuestros datos
URL = 'https://github.com/fcoterroba/random_spanish' #Modificar con vuestros datos

LICENSE = 'GNU GPL' #Tipo de licencia
DESCRIPTION = 'Library to obtain names of Spanish men and women as well as surnames'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') 
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
    'pandas'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
