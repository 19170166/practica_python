import sys
import json

from EXIM import EXIM
from Local import *
from prueba import *
import pandas as pd
from EXIM import *
from Peticiones import *

loc = Local()
pru = prueba()
ei = EXIM()


class Menu:
    def __init__(self):
        self.__local = Local()
        self.idusu = 1
        self.__ei = EXIM()

    def run(self):
        self.importar_dat()
        self.modo = self.seleccion_modo()
        self.__peticion = Peticiones(self.modo)
        self.opciones_menu()

    def opciones_menu(self):
        while True:
            print('1- Prestar')
            print('2- Devolver')
            print('3- Registrar Usuario')
            print('4- Mostrar Inventario')
            print('5- Mostrar Pendientes')
            print('6- Mostrar Entregas')
            print('7- Mostrar deudores')
            print('8- Exportar Datos')
            print('9- Menu Base de Datos')
            print('10- Importar Datos')
            print('11- Cambiar base de datos')
            print('12- Salir')
            opcion = int(input('Seleccione una opcion... '))
            if opcion == 1:
                self.entregar()
            if opcion == 2:
                self.regresar()
            if opcion == 3:
                self.agregar()
            if opcion == 4:
                self.most_inventario()
            if opcion == 5:
                self.most_pendiente()
            if opcion == 6:
                self.most_entregas()
            if opcion == 7:
                self.most_deu()
            if opcion == 8:
                self.exportar_dat()
            if opcion == 9:
                self.menu_base_datos()
            if opcion == 10:
                self.importar_dat()
            if opcion == 11:
                self.cambiar_base()
            if opcion == 12:
                sys.exit(0)

    def entregar(self):
        opcion = ' '
        while opcion != 's':
            print('------Prestar------')
            if len(self.__local.mostrar_personas()) > 0:  # verificar si hay personas
                for i, x in enumerate(self.__local.mostrar_personas()):
                    print(
                        f'{i}- nombre: {x.obt_nombre()} objetos: {x.obt_data()}')  # imprime el nombre de las personas registradas
                try:
                    persona = int(input('Seleccione una persona'))  # se selecciona una persona
                    p = self.__local.obt_persona(persona)  # se asigna la persona seleccionada
                    obj = input('Objeto que se prestara (balon/valla/bate/tela/porteria):')
                    if self.__local.verificar_valor(obj):  # se verifica la opcion elegida
                        cant = int(input('Cantidad: '))
                        if self.__local.disponibilidad(obj, cant):  # verificamos la disponibilidad del objeto
                            fecha = input('Ingresa la fecha')
                            p.agregar_obj(obj, cant)  # se entregan los objetos
                            self.__local.agregar_fecha_pen(persona, obj, fecha, cant)
                            self.__local.entregar(obj, cant)
                            print(p.obt_data())
                        else:
                            print('No hay objetos disponibles')
                    else:
                        print('El objeto no existe')
                except IndexError:
                    print('La persona seleccionada no existe')
            else:
                print('No hay personas registradas')
            opcion = input('Desea regresar al menu principal? s/n ')

    def most_inventario(self):
        print(self.__local.ver_inventario())

    def regresar(self):
        opcion = ''
        while opcion != 's':
            if len(self.__local.mostrar_personas()) > 0:
                print('-----Devolver-----')
                for i, x in enumerate(self.__local.mostrar_personas()):
                    print(f'{i}- nombre: {x.obt_nombre()} objetos: {x.obt_data()}')
                try:
                    nom = int(input('Seleccione una persona: '))
                    p = self.__local.obt_persona(nom)
                    obj = input('Objeto que se prestara (balon/valla/bate/tela/porteria):')
                    if self.__local.verificar_valor(obj):
                        cant = int(input('Cantidad: '))
                        if p.dis_persona(obj, cant):
                            fecha = input('Ingresa la fecha')
                            p.devolver_obj(obj, cant)  # se entregan los objetos
                            self.__local.agregar_fecha_ent(nom, obj, fecha, cant)
                            self.__local.regresar(obj, cant)
                            print(p.obt_data())
                        else:
                            print('No hay objetos disponibles')
                    else:
                        print('El objeto no existe')
                except IndexError:
                    print('La persona seleccionada no existe')
            else:
                print('No hay personas registradas')
            opcion = input('Desea regresar al menu principal? s/n ')

    def agregar(self):
        opcion = ''
        while opcion != 's':
            print('------Agregar Usuario------')
            nombre = input('Ingrese el nombre de la persona: ')
            self.__local.agregar_usuario(nombre, self.idusu)
            self.idusu += 1
            opcion = input('Desea regresar al menu principal? s/n ')

    def most_pendiente(self):
        if len(self.__local.obt_inv_prestamo()) > 0:
            for x in self.__local.obt_inv_prestamo():
                print(x)
        else:
            print("No hay prestamos")

    def most_entregas(self):
        if len(self.__local.obt_inv_entrega()):
            for x in enumerate(self.__local.obt_inv_entrega()):
                print(x)
        else:
            print("No hay entregas")

    def most_deu(self):
        for p in self.__local.mostrar_personas():
            for i in p.obt_data():
                if p.obt_data()[i] > 0:
                    self.__local.llenar_deudores(p.obt_per())
                    print(p.obt_per())
                    break

    def exportar_dat(self):
        for _, x in enumerate(self.__local.mostrar_personas()):
            self.__ei.exportar(x.obt_per())
        for _, b in enumerate(self.__local.obt_inv_prestamo()):
            self.__ei.exportar_pendientes(b)
        for _, d in enumerate(self.__local.obt_inv_entrega()):
            self.__ei.exportar_entregas(d)
        for _, c in enumerate(self.__local.obt_deu()):
            self.__ei.exportar_deudores(c)
        i = self.__local.ver_inventario()
        self.__ei.exportar_inventario(i)
        self.__ei.exportar_id(self.idusu)
        self.__ei.savedata()

    def importar_dat(self):
        self.__local = self.__ei.importar()
        self.idusu = self.__ei.set_id()

    def seleccion_modo(self):
        modo = input('Seleccione el tipo de base de datos (sql/mongo)')
        return modo

    def menu_base_datos(self):
        print('---------Menu Base de Datos-------------')
        print('---------Persona-------------')
        print('1) Mostrar todos los usuarios')
        print('2) Insertar Persona')
        print('3) Editar Persona')
        print('4) Eliminar Persona')
        print('---------Pedidos-------------')
        print('5) Mostrar todos los pedidos')
        print('6) Insertar Pedido')
        print('7) Editar Pedido')
        print('8) Eliminar Pedido')
        opc = int(input('seleccione una opcion'))
        if opc == 1:
            self.mostrar_personas()
        if opc == 2:
            self.insertar_persona()
        if opc == 3:
            self.modificar_persona()
        if opc == 4:
            self.eliminar_persona()
        if opc == 5:
            self.mostrar_pedido()
        if opc == 6:
            self.insertar_pedido()
        if opc == 7:
            self.modificar_pedido()
        if opc == 8:
            self.eliminar_pedido()

    def mostrar_personas(self):
        for x in enumerate(self.__peticion.mostrar()):
            print(x)

    def insertar_persona(self):
        nombre = input('Ingrese el nombre')
        balon = int(input('Ingrese la cantidad de balones'))
        valla = int(input('Ingrese la cantidad de vallas'))
        bate = int(input('Ingrese la cantidad de bates'))
        tela = int(input('Ingrese la cantidad de telas'))
        porteria = int(input('Ingrese la cantidad de porterias'))
        self.__peticion.insertar(id=self.idusu, nombre=nombre, balon=balon, valla=valla, bate=bate, tela=tela,
                                 porteria=porteria)

    def eliminar_persona(self):
        self.mostrar_personas()
        idu = int(input('Ingrese el id del usuario'))
        self.__peticion.eliminar(idu)

    def modificar_persona(self):
        self.mostrar_personas()
        idu = int(input('Ingrese el id del usuario'))
        campo = input('Ingrese el campo que desea modificar (balon/valla/bate/tela/porteria)')
        valor = int(input('Ingrese la cantidad'))
        self.__peticion.modificar(campo=campo, valor=valor, id=idu)

    def mostrar_pedido(self):
        for x in enumerate(self.__peticion.mostrar_pedidos()):
            print(x)

    def insertar_pedido(self):
        self.mostrar_personas()
        id = int(input('Ingrese el id del usuario'))
        objeto = input('Ingrese el objeto prestado')
        valor = int(input('Ingrese la cantidad prestada'))
        fecha = input('Ingrese la fecha')
        self.__peticion.insertar_pedido(idp=id, objeto=objeto, valor=valor, fecha=fecha)

    def eliminar_pedido(self):
        self.mostrar_pedido()
        id = int(input('Ingrese el id'))
        self.__peticion.eliminar_pedido(id)

    def modificar_pedido(self):
        self.mostrar_pedido()
        idu = int(input('Ingrese el id del prestamo'))
        campo = input('Ingrese el campo que desea modificar')
        valor = int(input('Ingrese la cantidad'))
        self.__peticion.modificar_pedido(campo=campo, valor=valor, id=idu)

    def cambiar_base(self):
        self.modo = self.seleccion_modo()
        self.__peticion = Peticiones(self.modo)


menu = Menu()
menu.run()
