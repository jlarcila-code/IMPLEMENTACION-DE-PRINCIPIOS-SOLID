"""Principio de inversión de dependencia
Los módulos de alto nivel no deberían depender de los modulos de bajo nivel,
ambos deberían depender de abstracciones y las abstracciones no deberían depender
de los detaller y los detalles deberían depender de las abstracciones"""

from enum import Enum
from abc import abstractmethod


# Enumeramos la clase club
class Clubs(Enum):
    NATACION = 1
    CICLISMO = 2
    ATLETISMO = 3

# Definimos la clase Student
class Student():
    def __init__(self, name):
        self.name = name

# Creamos un metodo para consultar las membresías
class ClubMembershipsLookup():
    @abstractmethod
    def find_all_students_from_club(self, club):
        pass

# Creamos una lista de diccionario para consultar las inscripciones
class ClubMemberships(ClubMembershipsLookup):
    def __init__(self):
        self.club_memberships = []

    def add_club_memberships(self, student, club):
        self.club_memberships.append((student, club))

    def find_all_students_from_club(self, club):
        for members in self.club_memberships:
            if members[1] == club:
                yield members[0].name
# 
class InspectMemberships():
    def __init__(self, club_memberships_lookup):
        for student in club_memberships_lookup.find_all_students_from_club(Clubs.ATLETISMO):
            print(f'{student} está en atletismo.')
        
        for student in club_memberships_lookup.find_all_students_from_club(Clubs.CICLISMO):
            print(f'{student} está en ciclismo.')

        for student in club_memberships_lookup.find_all_students_from_club(Clubs.NATACION):
            print(f'{student} está en natación.')

    
Student_one = Student ('Davis Galán')
Student_two = Student ('José Luis')
Student_three = Student ('María')

club_memberships = ClubMemberships()

club_memberships.add_club_memberships(Student_one, Clubs.ATLETISMO)
club_memberships.add_club_memberships(Student_two, Clubs.CICLISMO)
club_memberships.add_club_memberships(Student_three, Clubs.NATACION)
   
InspectMemberships(club_memberships)  