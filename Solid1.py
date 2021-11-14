class Libros():
    def __init__(self):
        self.libros = {}
        self.numero = 0
    
    def add_libro(self, libro):
        self.numero += 1
        self.libros[self.numero] = libro

    def __str__(self):
        return str(self.libros)

class Libreria():
    @staticmethod
    def guardar_libros(filename, libros):
        with open(filename, "w") as f:
           f.write(str(libros))

b = Libros()
b.add_libro("Libro A")
b.add_libro("Libro B")
print(f"Los libros que he leído son: {b}")

s = Libreria()
s.guardar_libros("filename_b.txt", b)