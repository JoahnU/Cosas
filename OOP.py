# A lil introduction to object oriented programming
class person:
    grupo = 0
    estatura = 0
    edad = 0
    __nombre =""
    def __init__(self, e, y, n):
        self.estatura = e
        self.edad = y
        self.nombre = n
j = person(174, 20, "juan")
h = person(165, 15, "juan2")

def __lt__(self, person):
    return self.edad < person.edad


print(j.edad)