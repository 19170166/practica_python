import mysql.connector


class PSQL:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='mydatabase',
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('create database if not exists mydatabase')
        self.mycursor.execute('create table if not exists personas (id int PRIMARY KEY, nombre varchar('
                              '150), balon int,valla int,bate int, tela int, porteria int)')
        self.mycursor.execute('create table if not exists pedidos (id int PRIMARY KEY AUTO_INCREMENT, persona_id int, '
                              'objeto varchar(40), cantidad int, fecha date,foreign key (persona_id) references '
                              'personas (id))')

    def insertar(self, idu, nombre, balon, valla, bate, tela, porteria):
        sql = 'insert into personas (id,nombre,balon,valla,bate,tela,porteria) values(%s,%s,%s,%s,%s,%s,%s)'
        val = [idu,nombre,balon,valla,bate,tela,porteria]
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def modificar(self, campo, id, valor):
        sql = f'update personas set {campo} = "{valor}" where id = {id}'
        self.mycursor.execute(sql)
        self.mydb.commit()

    def eliminar(self, id):
        sql = f'delete from personas where id = {id}'
        self.mycursor.execute(sql)
        self.mydb.commit()

    def mostrar(self):
        self.mydb.commit()
        self.mycursor.execute('SELECT * FROM personas')
        return self.mycursor.fetchall()

    def insertar_pedido(self,idp,objeto,cantidad,fecha):
        sql=f'insert into pedidos (persona_id,objeto,cantidad,fecha) values(%s,%s,%s,%s)'
        valores=[idp,objeto,cantidad,fecha]
        self.mycursor.execute(sql,valores)
        self.mydb.commit()

    def modificar_pedido(self,campo,valor,id):
        sql = f'update pedidos set {campo} = "{valor}" where id = {id}'
        self.mycursor.execute(sql)
        self.mydb.commit()

    def eliminar_pedido(self,id):
        sql = f'delete from pedidos where id = {id}'
        self.mycursor.execute(sql)
        self.mydb.commit()

    def mostrar_pedido(self):
        self.mydb.commit()
        return self.mycursor.execute('select * from pedidos')


# psql = PSQL()
# psql.crear_tabla()
# psql.insertar()
# psql.modificar()
# psql.eliminar()
# psql.mostrar()
