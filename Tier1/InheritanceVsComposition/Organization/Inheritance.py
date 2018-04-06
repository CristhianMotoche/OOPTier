#!/usr/bin/env python3


class Persona(object):
    def __init__(self, nombre, ci):
        pass

class Empleado(Persona):
    def __init__(self, sueldo, horario_trabajo):
        pass

class Administrador(Empleado):
    def __init__(self, personal):
        pass

    def organizar(self):
        pass

class Ingeniero(Empleado):
    def __init__(self, tareas_tecnicas):
        pass

    def construir_cosas_cheveres(self):
        pass

# Y el TechLeader es una especie de admnistrador que también realiza cosas técnicas
# (honestamente no tengo idea, solo lo estoy suponiendo para este ejemplo).
class TechLeader(Administrador, Ingeniero):
    def __init__(self):
        pass

# Cuando se instancia un objeto de esta clase
techlead = TechLeader()

# Y se accede a un atributo que pertenece a ambas clases.

