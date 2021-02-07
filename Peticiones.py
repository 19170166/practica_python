from Peticiones_SQL import *
from Peticiones_Mongo import *




class Peticiones:
    def __init__(self, peti):
        if peti == 'sql':
            self.__peticiones = PSQL()
        if peti == 'mongo':
            self.__peticiones = Mongo()

    def mostrar(self):
        return self.__peticiones.mostrar()

    def eliminar(self,id):
        self.__peticiones.eliminar(id)

    def modificar(self,campo,valor,id):
        self.__peticiones.modificar(campo=campo,valor=valor,id=id)

    def insertar(self,id,nombre,balon,valla,bate,tela,porteria):
        self.__peticiones.insertar(id,nombre,balon,valla,bate,tela,porteria)

    def mostrar_pedidos(self):
        return self.__peticiones.mostrar_pedido()

    def eliminar_pedido(self,id):
        self.__peticiones.eliminar_pedido(id)

    def modificar_pedido(self,id,campo,valor):
        self.__peticiones.modificar_pedido(id=id,campo=campo,valor=valor)

    def insertar_pedido(self,idp,objeto,valor,fecha):
        self.__peticiones.insertar_pedido(idp=idp,objeto=objeto,cantidad=valor,fecha=fecha)
