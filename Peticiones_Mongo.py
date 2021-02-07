import pymongo


class Mongo:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb+srv://admin:admin123@mongo.gl0oz.mongodb.net/mydatabase?retryWrites=true&w=majority")
        self.mydb = self.myclient["mydatabase"]
        self.mycol = self.mydb["personas"]
        self.mycol2 = self.mydb["pedidos"]

    def insertar(self, idu, nombre, balon, valla, bate, tela, porteria):
        mydict = {"_id": idu, "nombre": nombre,
                  "objeto": {"balon": balon, "valla": valla, "bate": bate, "tela": tela, "porteria": porteria}}
        self.mycol.insert_one(mydict)

    def mostrar(self):
        return self.mycol.find()

    def eliminar(self, id):
        myquery = {"_id": id}
        self.mycol.delete_one(myquery)

    def modificar(self, campo, valor, id):
        myquery = {"_id": id}
        newvalues = {"$set": {campo: valor}}
        self.mycol.update_one(myquery, newvalues)

    def insertar_pedido(self, idp, objeto, cantidad, fecha):
        mydict = {"_id": self.mycol2.find().count() + 1, "persona_id": idp, "objeto": objeto, "cantidad": cantidad,
                  "fecha": fecha}
        self.mycol2.insert_one(mydict)

    def modificar_pedido(self, id, campo, valor):
        mydict = {"_id": id}
        newvalues = {"$set": {campo: valor}}
        self.mycol2.update_one(mydict,newvalues)

    def eliminar_pedido(self,id):
        mydict = {"_id":id}
        self.mycol.delete_one(mydict)

    def mostrar_pedido(self):
        return self.mycol2.find()

# mongo = Mongo()
# mongo.insertar()
# mongo.eliminar()
# mongo.mostrar()
# mongo.modificar()
