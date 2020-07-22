import sys
from conexion import Conector

class danPlancuenta(Conector):
    def __init__(self):
        super().__init__()
    #Consultar
    def consultar(self, buscar):
        result = False
        try:
            sql ="select * from plancuenta where descripcion like'"+str(buscar)+"%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta del cuenta", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
    #Ingresar
    def ingresar(self, cuen):
        correto = True
        try:
            sql="insert into plancuenta (codigo, grupo, descripcion, naturaleza, estado) values (%s, %s, %s, %s, %s)"
            self.conectar()
            self.conector.execute(sql,(cuen.codigo, cuen.grupo, cuen.descripcion, cuen.naturaleza, cuen.estado))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar plan de cuanta", e)
            correto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correto
    #Modificar
    def modificar(self, cuen):
        correto = True
        try:
            sql="update plancuenta set grupo=%s, descripcion=%s, naturaleza=%s, estado=%s where id = %s"
            self.conectar()
            self.conector.execute(sql,(cuen.grupo, cuen.descripcion, cuen.naturaleza, cuen.estado, cuen.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar plan de cuanta", e)
            correto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correto
    #Eliminar
    def eliminar(self, cuen):
        correto = True
        try:
            sql="DELETE FROM  plancuenta where id = %s"
            self.conectar()
            self.conector.execute(sql,(cuen.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar plan de cuanta", e)
            correto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correto
    def consultargrupo(self):
        result = False
        try:
            sql ="select id, descripcion from grupo order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
    def consultarcodigo(self):
        result = False
        try:
            sql ="SELECT  codigo FROM plancuenta ORDER BY codigo DESC  LIMIT  1"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
class danGrupo(Conector):
    def __init__(self):
        super().__init__()
    def consultargrupo(self, buscar):
        result = False
        try:
            sql ="select * from grupo where descripcion like'"+str(buscar)+"%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta de grupo", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
    def ingresargrupo(self, gp):
        correto = True
        try:
            sql="insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql,(gp.descripcion))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar plan de cuanta", e)
            correto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correto
    def modificargrupo(self, gp):
        correto = True
        try:
            sql="update grupo set descripcion=%s where id = %s"
            self.conectar()
            self.conector.execute(sql,(gp.descripcion, gp.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar plan de cuanta", e)
            correto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correto
    def eliminargrupo(self, gp):
        correto = True
        try:
            sql="DELETE FROM  grupo where id = %s"
            self.conectar()
            self.conector.execute(sql,(gp.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar plan de cuanta", e)
            correto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correto



#con= danPlancuenta()
#grupos=con.consultargrupo()
#for gru in grupos:
#    print(gru[0])



