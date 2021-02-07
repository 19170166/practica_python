from Persona import *
import sys


class Local:
    def __init__(self):
        self.__invent = []
        self.__ent = {}
        self.__invpen = []
        self.__pen = {}
        self.__inv = {
            'balon': 50,
            'valla': 50,
            'porteria': 50,
            'tela': 50,
            'bate': 50,
        }
        self.__personas = []
        self.__deudores = []

    def disponibilidad(self, objeto, cantidad):
        if cantidad < self.__inv[objeto] and objeto in self.__inv.keys():
            return True

    def restaurar_inv(self,obj,cant):
        self.__inv[obj] = cant

    def ver_inventario(self):
        return self.__inv

    def agregar_fecha_pen(self, id, objeto, fecha, cantidad):
        x = self.__pen = {'nombre': f'{self.obt_persona(id).obt_nombre()}', f'{objeto}': f'{cantidad}',f'fecha': f'{fecha}'}
        self.__invpen.append(x)

    def obt_inv_prestamo(self):
        return self.__invpen

    def llenar_pendientes(self, pend):
        self.__invpen.append(pend)

    def llenar_entregas(self, ent):
        self.__invent.append(ent)

    def llenar_deudores(self, deu):
        self.__deudores.append(deu)

    def restaurar_inventario(self,obj):
        #self.__inv[obj] = can
        self.__inv = obj

    def obt_deu(self):
        return self.__deudores

    def obt_pendientes(self, posicion):
        return self.__invpen[posicion]

    def agregar_fecha_ent(self, id, objeto, fecha, cantidad):
        x = self.__ent = {'nombre': f'{self.obt_persona(id).obt_nombre()}', f'{objeto}': f'{cantidad}',
                          f'fecha': f'{fecha}'}
        self.__invent.append(x)

    def obt_inv_entrega(self):
        return self.__invent

    def obt_entregas(self, posicion):
        return self.__invent[posicion]

    def agregar_usuario(self, nombre,id):
        self.__personas.append(Persona(nombre,id))

    def mostrar_personas(self):
        return self.__personas

    def obt_persona(self, posicion):
        return self.__personas[posicion]

    def entregar(self, objeto, cantidad):
        if objeto in self.__inv.keys():
            self.__inv[objeto] -= cantidad

    def regresar(self, objeto, cantidad):
        if objeto in self.__inv.keys():
            self.__inv[objeto] += cantidad

    def verificar_valor(self, objeto):
        print(objeto)
        print(self.__inv)
        if objeto in self.__inv.keys():
            return True
        return False
