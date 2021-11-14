"""Principio Open Closed
Una clase debe estar abierta para extensión y cerrada para modificación

software que permiter cargar y almacenar archivos a diferentes proveedores en la nube

Para respetar el principio se crean clases y metodos abstractos. """
from abc import ABC, abstractmethod

class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class Uploader(ABC):
    @abstractmethod
    def upload_file(self):
        pass

# Autenticación Amazon Web Services
class Aws(Auth, Uploader):

    def authenticate(self): 
        return super().authenticate

    def upload_file(self):
        return super().upload_file()

# Autenticación Azure
class Azure(Auth, Uploader):

    def authenticate(self):
        return super().authenticate

    def upload_file(self):
        return super().upload_file()

# Autenticación GCP
class Google_Cloud(Auth, Uploader):

    def authenticate(self):
        return super().authenticate

    def upload_file(self):
        return super().upload_file()