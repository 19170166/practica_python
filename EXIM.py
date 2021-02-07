import json
from Local import *
from Persona import *


class EXIM:
    def __init__(self):
        self.__local = Local()
        self.__data = {'personas': [], 'deudores': [], 'pedidos': [], 'entregas': [], 'inventario': {},"idu":0}

    def exportar(self, objson):
        self.__data['personas'].append(objson)

    def exportar_pendientes(self, objsonpen):
        self.__data['pedidos'].append(objsonpen)

    def exportar_entregas(self, objsonent):
        self.__data['entregas'].append(objsonent)

    def exportar_deudores(self, objsondeu):
        self.__data['deudores'].append(objsondeu)

    def exportar_inventario(self,objsoninv):
        self.__data['inventario']=objsoninv

    def savedata(self):
        with open('data.json', 'w') as archivo:
            json.dump(self.__data, archivo, indent=4)

    def exportar_id(self,objid):
        self.__data['idu'] = objid

    def set_id(self):
        with open('data.json') as arc_data:
            data_pers = json.load(arc_data)
        return data_pers['idu']

    def importar(self):

        with open('data.json') as arc_data:
            data_pers = json.load(arc_data)
            i = 0
            for pers in data_pers['personas']:
                self.__local.agregar_usuario(pers['nombre'],pers['id'])
                u = self.__local.obt_persona(i)
                for item in pers['objeto']:
                    u.restaurar_inv(obj=item, cant=pers['objeto'][item])
                i += 1
            for ped in data_pers['pedidos']:
                self.__local.llenar_pendientes(ped)
            for en in data_pers['entregas']:
                self.__local.llenar_entregas(en)
            for deu in data_pers['deudores']:
                self.__local.llenar_deudores(deu)
            #for inv in data_pers['inventario']:
            #    for invr in self.__local.ver_inventario():
            #        self.__local.restaurar_inventario(invr,inv[invr])
            self.__local.restaurar_inventario(data_pers['inventario'])
        return self.__local
