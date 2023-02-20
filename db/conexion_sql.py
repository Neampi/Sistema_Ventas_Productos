

from sqlite3 import Cursor
import pyodbc

class Conexion():
    def __init__(self):
        try:
            self.connec=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-9N4UR2R;DATABASE=bd_selltec;UID=sa;PWD=serv2023')
            print("SERVIDOR CONECTADO")
        except Exception as e:
            print("ERROR AL CONECTAR A SQL SERVER",e)

    def inicio_sesion(self, usu, pas):
        cursor=self.connec.cursor()
        cursor.execute('SELECT * FROM ventasreg.usuarios WHERE username=? AND password=?',(usu,pas))
        log=cursor.fetchall()
        cursor.close()
        return log

    #VER EL CARGO DEL USUARIO
    def cargo_usu(self, carg):
        cursor=self.connec.cursor()
        cursor.execute('SELECT nombre FROM ventasreg.cargos WHERE idcargo=?',(carg))
        nombrecargo=cursor.fetchall()[0][0]
        cursor.close()
        return nombrecargo

    #VISUALIZAR INVENTARIO
    def inventario(self):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.codigo, co.descripcion, tpro.nombre,  co.marca, co.modelo ,co.precioVenta, co.cantidad FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos;')
        invent=cursor.fetchall()
        return invent

    #VISUZALIZAR LAS CATEGORIAS EN COMBOBOX
    def combobd_categoria_inventario(self):
        cursor=self.connec.cursor()
        cursor.execute('SELECT * FROM ventasreg.tipo_productos')
        cat=cursor.fetchall()
        return cat

    #VISUZALIZAR LAS MARCAS EN COMBOBOX
    def combobd_marca_inventario(self,indicador):
        cursor=self.connec.cursor()
        cursor.execute('SELECT DISTINCT co.marca FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos WHERE tpro.nombre=?',indicador)
        mar=cursor.fetchall()
        return mar

    #VISUZALIZAR LOS MODELOS EN COMBOBOX
    def combobd_modelo_inventario(self,indicadorx, indicadory):
        cursor=self.connec.cursor()
        cursor.execute('SELECT DISTINCT co.modelo FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos WHERE tpro.nombre=? AND co.marca=?',(indicadorx,indicadory))
        mod=cursor.fetchall()
        return mod

    #BUSQUEDA DE PRODUCTOS POR COMBOBOX EN INVENTARIO
    def busqueda_producto_cbx(self, x, y, z):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.codigo, co.descripcion, tpro.nombre,  co.marca, co.modelo ,co.precioVenta, co.cantidad FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos WHERE tpro.nombre=? AND co.marca=? AND co.modelo=?;',(x, y, z))
        busqueda_cbx=cursor.fetchall()
        return busqueda_cbx

    #VISUALIZACION DE COMPRAS REGISTRADAS
    def compras_inventario(self):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.fecha, usu.nombre, tpro.nombre, co.codigo, co.descripcion, co.marca, co.modelo, co.precioCompra, co.precioVenta, co.cantidad, co.totalcompra FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos INNER JOIN ventasreg.usuarios usu ON co.usuario_ingreso=usu.idUsuarios;')
        compras=cursor.fetchall()
        return compras

    #BUSQUEDA DE COMPRAS POR COMBOBOX Y FECHAS
    def busqueda_compras_fecha_total(self,cate,mar,mod, d1, d2):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.fecha, usu.nombre, tpro.nombre, co.codigo, co.descripcion, co.marca, co.modelo, co.precioCompra, co.precioVenta, co.cantidad, co.totalcompra FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos INNER JOIN ventasreg.usuarios usu ON co.usuario_ingreso=usu.idUsuarios WHERE tpro.nombre=? AND co.marca=? AND co.modelo=? AND co.fecha>=? AND co.fecha<=?;',(cate,mar,mod,d1, d2))
        compras_cbx=cursor.fetchall()
        return compras_cbx

    #BUSQUEDA DE COMPRAS POR FECHAS
    def busqueda_compras_fecha(self,d1, d2):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.fecha, usu.nombre, tpro.nombre, co.codigo, co.descripcion, co.marca, co.modelo, co.precioCompra, co.precioVenta, co.cantidad, co.totalcompra FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos INNER JOIN ventasreg.usuarios usu ON co.usuario_ingreso=usu.idUsuarios WHERE co.fecha>=? AND co.fecha<=?;',(d1, d2))
        compras_cbx=cursor.fetchall()
        return compras_cbx

    #BUSQUEDA DE COMPRAS POR CATEGORIA
    def busqueda_compras_categoria(self,cate):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.fecha, usu.nombre, tpro.nombre, co.codigo, co.descripcion, co.marca, co.modelo, co.precioCompra, co.precioVenta, co.cantidad, co.totalcompra FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos INNER JOIN ventasreg.usuarios usu ON co.usuario_ingreso=usu.idUsuarios WHERE tpro.nombre=?;',(cate))
        compras_cbx=cursor.fetchall()
        return compras_cbx

    #BUSQUEDA DE COMPRAS POR MARCA
    def busqueda_compras_marca(self,cate, mar):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.fecha, usu.nombre, tpro.nombre, co.codigo, co.descripcion, co.marca, co.modelo, co.precioCompra, co.precioVenta, co.cantidad, co.totalcompra FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos INNER JOIN ventasreg.usuarios usu ON co.usuario_ingreso=usu.idUsuarios WHERE tpro.nombre=? AND co.marca=?;',(cate, mar))
        compras_cbx=cursor.fetchall()
        return compras_cbx

    def busqueda_codigo_newbuy(self,cod):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.fecha, usu.nombre, tpro.nombre, co.codigo, co.descripcion, co.marca, co.modelo, co.precioCompra, co.precioVenta, co.cantidad, co.totalcompra FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos INNER JOIN ventasreg.usuarios usu ON co.usuario_ingreso=usu.idUsuarios WHERE co.codigo=?;',(cod))
        new_prod=cursor.fetchall()
        return new_prod

    def registro_producto(self,usuario, categoria, cod, desc, marca, modelo, pc, pv, stock, tc):
        cursor=self.connec.cursor()
        cursor.execute('INSERT INTO ventasreg.compra (fecha, usuario_ingreso, tipo, codigo ,descripcion, marca, modelo, precioCompra, precioVenta, cantidad, totalcompra) VALUES (GETDATE(), ?,(SELECT idtipo_productos FROM ventasreg.tipo_productos WHERE nombre=?),?,?,?,?,?,?,?,?);',(usuario,categoria,cod,desc,marca,modelo,pc,pv,stock,tc))
        self.connec.commit()
        cursor.close()

    #BUSQUEDA DE PRODUCTO POR CODIGO PARA LA VENTANA DE SELECCION
    def busqueda_codigo_seleccion(self,cod):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.codigo, co.descripcion, tpro.nombre, co.marca, co.modelo, co.precioVenta FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos WHERE co.codigo=?;',(cod))
        cod_prod=cursor.fetchall()
        return cod_prod

    #BUSQUEDA DE PRODUCTO POR COMBOBOX PARA LA VENTANA DE SELECCION
    def busqueda_producto_venta_cbx(self, x, y, z):
        cursor=self.connec.cursor()
        cursor.execute('SELECT co.idproductos, co.codigo, co.descripcion, tpro.nombre, co.marca, co.modelo ,co.precioVenta FROM ventasreg.compra co INNER JOIN ventasreg.tipo_productos tpro ON co.tipo=tpro.idtipo_productos WHERE tpro.nombre=? AND co.marca=? AND co.modelo=?;',(x, y, z))
        busqueda_cbx=cursor.fetchall()
        return busqueda_cbx

    def tipo_pago(self):
        cursor=self.connec.cursor()
        cursor.execute('SELECT nombre FROM ventasreg.tipo_pago')
        tpago=cursor.fetchall()
        return tpago

    def proceso_detalle_venta(self,cod,pro,des,mar,mod,pre,dscto,cant,tot,cv):
        cursor=self.connec.cursor()
        cursor.execute('INSERT INTO ventasreg.detalle_venta (codigo, producto, descripcion, marca, modelo, precio, dscto, cantidad, total, cod_venta) VALUES (?,(SELECT idtipo_productos FROM ventasreg.tipo_productos WHERE nombre=?),?,?,?,?,?,?,?,?)',(cod,pro,des,mar,mod,pre,dscto,cant,tot,cv))
        self.connec.commit()
        cursor.close()

    def proceso_venta(self,codv,cliente,doc,tel,tot,tp,vend):
        cursor=self.connec.cursor()
        cursor.execute('INSERT INTO ventasreg.venta (id_cod_venta, fecha, cliente_name, documento, telefono, total, tipo_pago, vendedor) VALUES(?,GETDATE(),?,?,?,?,(SELECT idtipo FROM ventasreg.tipo_pago WHERE nombre=?),?)',(codv,cliente,doc,tel,tot,tp,vend))
        self.connec.commit()
        cursor.close()

    def obtener_ultimo_id_venta(self):
        cursor = self.connec.cursor()
        cursor.execute('SELECT MAX(idventa) FROM ventasreg.venta')
        resultado = cursor.fetchone()
        if resultado[0] is not None:
            return int(resultado[0])
        else:
            return 1