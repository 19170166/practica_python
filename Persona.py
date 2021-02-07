import sys


class Persona:
    def __init__(self, nombre):
        self.__data = {
            'id':0,
            'nombre': nombre,
            'objeto': {
                'balon': 0,
                'valla': 0,
                'bate': 0,
                'tela': 0,
                'porteria': 0
            }
        }

    def __init__(self,nombre,id):
        self.__data = {
            'id': id,
            'nombre': nombre,
            'objeto': {
                'balon': 0,
                'valla': 0,
                'bate': 0,
                'tela': 0,
                'porteria': 0
            }
        }

    def obt_per(self):
        return self.__data

    def obt_id(self):
        return self.__data['id']

    def obt_nombre(self):
        return self.__data["nombre"]

    def obt_data(self):
        return self.__data['objeto']

    def agregar_obj(self, objeto, cantidad):
        if objeto in self.__data['objeto'].keys():
            self.__data['objeto'][objeto] += cantidad

    def devolver_obj(self, objeto, cantidad):
        if objeto in self.__data['objeto'].keys():
            self.__data['objeto'][objeto] -= cantidad

    def asig_nomre(self, nombre):
        self.__data['nombre'] = nombre

    def dis_persona(self, objeto, cantidad):
        if objeto in self.__data['objeto'].keys() and cantidad <= self.__data['objeto'][objeto]:
            return True
        return False

    def restaurar_inv(self,obj,cant):
        self.__data['objeto'][obj] = cant
