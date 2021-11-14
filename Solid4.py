"""Principio de segregación de interface
Dividir la interface hasta el grado de granularidad mas pequeño posible"""

from abc import ABC, abstractmethod

class Celular(ABC):
    @abstractmethod
    def llamar(self):
        pass

class Texto(ABC):
    @abstractmethod
    def mensaje_texto(self):
        pass

class Camara(ABC):
    @abstractmethod
    def foto(self):
        pass

class SmartPhone(Celular, Texto, Camara):
    def llamar(self):
        pass

    def mensaje_texto(self):
        pass

    def foto(self):
        pass

class CelularViejo(Celular, Texto):
    def llamar(self):
        pass

    def mensaje_texto(self):
        pass

class Celulardesechable(Texto):
    def llamar(self):
        pass