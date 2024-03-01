class Equipo:
    def __init__(self, nombre, integrantes, eslogan):
        self.nombre = nombre
        self.integrantes = integrantes
        self.eslogan = eslogan

class FS3:
    def __init__(self):
        self.webheros = Equipo("WebHeros", ["Jesus Manuel Arellano Merendon", "Axel Felipe Reyes Valadez", "Luis Daniel Delgado Enriquez"], 
                               "La verdad solo se puede encontrar en un lugar: el codigo")
        self.pinguinos_galacticos = Equipo("Pingüinos galacticos", ["Yesica Cristina Rodriguez Renteria", "Yahir Antonio Monje Ochoa"], 
                                           "SIC•PARVIS•MAGNA")
        self.los_polystation = Equipo("Los polystation", ["Paulina Ixchel Arreguin Ruiz", "Erick Fernando Siqueiros Zúñiga",], 
                                      "Conectando el futuro, hoy")
        self.los_3_mosqueteros = Equipo("Los 3 mosqueteros", ["Dania Denisse Benavides Figueroa", "Erick Lozano Duarte", "Ana Cristina Valenzuela Ruiz"], 
                                        "Todos para uno, uno para todos")
        self.toyota_legacy = Equipo("Toyota Legacy", ["Israel Chacon Rojo", "Dilan Mauricio Garcia Hernandez", "Jesus Elías Sierra Ruiz"], 
                                        "Transformamos líneas de código en experiencias excepcionales")
        self.los_uwu = Equipo("Los =^UwU^=", ["Leonardo Alberto Gonzáles Carmona", "Norma Graciela Mendoza Ruiz", "Jonathan Durán Mendoza"], 
                                        "Respiración de Programación, Pose de HTML, Codificar")

    def __str__(self):
        equipos_info = [
            f"Equipo: {self.webheros.nombre}\nIntegrantes:\n{'\n'.join(self.webheros.integrantes)}\nEslogan: {self.webheros.eslogan}\n",
            f"Equipo: {self.pinguinos_galacticos.nombre}\nIntegrantes:\n{'\n'.join(self.pinguinos_galacticos.integrantes)}\nEslogan: {self.pinguinos_galacticos.eslogan}\n",
            f"Equipo: {self.los_polystation.nombre}\nIntegrantes:\n{'\n'.join(self.los_polystation.integrantes)}\nEslogan: {self.los_polystation.eslogan}\n",
            f"Equipo: {self.los_3_mosqueteros.nombre}\nIntegrantes:\n{'\n'.join(self.los_3_mosqueteros.integrantes)}\nEslogan: {self.los_3_mosqueteros.eslogan}\n",
            f"Equipo: {self.toyota_legacy.nombre}\nIntegrantes:\n{'\n'.join(self.toyota_legacy.integrantes)}\nEslogan: {self.toyota_legacy.eslogan}\n",
            f"Equipo: {self.los_uwu.nombre}\nIntegrantes:\n{'\n'.join(self.los_uwu.integrantes)}\nEslogan: {self.los_uwu.eslogan}\n",
        ]
        return '\n'.join(equipos_info)

fs3 = FS3()

print(str(fs3))






    