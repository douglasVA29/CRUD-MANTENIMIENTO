from dan_Plancuenta import danPlancuenta
from mod_plancuenta import ModPlancuenta
from dan_Plancuenta import danGrupo

class ctrPlancuenta:
    def __init__(self,cuen=None):
        self.cuenta=cuen
    def consulta(self, buscar):
        objdan=danPlancuenta()
        return objdan.consultar(buscar)
    def ingresar(self, cuen):
        objdan=danPlancuenta()
        return objdan.ingresar(cuen)
    def modificar(self, cuen):
        objdan=danPlancuenta()
        return  objdan.modificar(cuen)
    def eliminar(self, cuen):
        objdan=danPlancuenta()
        return objdan.eliminar(cuen)
    def consultarcodigo(self):
        objdan=danPlancuenta()
        return objdan.consultarcodigo()
    def consultargrupo(self):
        objdan=danPlancuenta()
        return objdan.consultargrupo()

class ctrGrupos:
    def __init__(self,gp=None):
        self.grupo=gp
    def consultaG(self, buscar):
        objdan=danGrupo()
        return objdan.consultargrupo(buscar)
    def ingresarG(self, gp):
        objdan=danGrupo()
        return objdan.ingresargrupo(gp)
    def modificarG(self, gp):
        objdan=danGrupo()
        return  objdan.modificargrupo(gp)
    def eliminarG(self, gp):
        objdan=danGrupo()
        return objdan.eliminargrupo(gp)