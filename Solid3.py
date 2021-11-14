""" Principio de sustitución Liskov 
Una clase derivada que puede asumir un lugar con una superclase, y todo debería funcionar"""


class Electrodomestico():
    def on():
        pass
    def off():
        pass

class ElectrodomesticosTemperatura(Electrodomestico):
    def set_temperature():
        pass

class Sanduchera(ElectrodomesticosTemperatura):
    def on():
        pass
    def off():
        pass
    def set_temperature():
        pass

class Licuadora(ElectrodomesticosTemperatura):
    def on():
        pass
    def off():
        pass