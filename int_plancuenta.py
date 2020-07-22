from ctr_plancuenta import ctrPlancuenta
from ctr_plancuenta import ctrGrupos
from mod_plancuenta import ModPlancuenta
from mod_grupo import ModGrupo
from menuprincipal import menu
import os
ctr=ctrPlancuenta()
ctrG=ctrGrupos()

def insertar(rango):
    for i in range(int(rango)):
        cod = ctr.consultarcodigo()
        if len(cod)==0:
            codigon = input('Ingresar el codigo 01: ')
        else:
            codigon = input('Ultimo codigo '+str("{}".format(cod[0]))+', ingresar el sigiente codigo: ')
        gruo = ctr.consultargrupo()
        for gru in gruo:    
           print("{}) {}".format(gru[0], gru[1]))
        grupo = input('Escriba el numero del gurpo del plan de cuanta: ')
        descripcion = input('Escriba la descripcion del plan de cuenta: ')
        naturaleza = input('Escriba la naturaleza del plan de cuenta D/A: ')
        estado = input('Ingresa el estado 1 para verdadero y 0 para falso: ')
        if input('Esta seguro que desea ingresar el registro si/no: ')=='si':
            plan = ModPlancuenta(cod=codigon, grup=grupo, desc=descripcion, natura=naturaleza, est=int(estado))
            if ctr.ingresar(plan):
                print('Registro correcto')
            else:
                print('Error al gravar')
        else:
            ejecutarMenuP()
def modificar():
    idPlan = input('Ingresa el id del plan de cuanta que desea modificar: ') 
    gruo = ctr.consultargrupo()
    for gru in gruo:    
        print("{}) {}".format(gru[0], gru[1]))
    grupo = input('Escriba el numero del gurpo del plan de cuanta: ')
    descripcion = input('Escriba la descripcion del plan de cuenta: ')
    naturaleza = input('Escriba la naturaleza del plan de cuenta D/A: ')
    estado = input('Ingresa el estado 1 para verdadero y 0 para falso: ')
    if input('Esta seguro que desea modificar el registro si/no: ')=='si':
       plan = ModPlancuenta(grup=grupo, desc=descripcion, natura=naturaleza, est=int(estado),ind=idPlan)
       if ctr.modificar(plan):
         print('Registro correcto')
       else:
         print('Error al gravar')
    else:
        ejecutarMenuP()
def eliminar():
    idPlan = input('Ingresa el id del plan de cuanta que desea eliminar: ') 
    if input('Esta seguro que desea eliminar el registro si/no: ')=='si':
        plan = ModPlancuenta(ind=int(idPlan))
        if ctr.eliminar(plan):
          print('Registro eliminado')
        else:
          print('Error al eliminar')
    else:
        ejecutarMenuP()
def consulta():
    buscar = input('Ingrese la descripcion a buscar en el plan de cuentas: ')
    plan = ctr.consulta(buscar)
    print('\n\tId\tCodigo\tGrupo\tDescripcion\tNaturaleza\tEstado')
    for regis in plan:
        print ('\n\t{}\t{}\t{}\t{}\t\t{}\t\t{}'.format(regis[0], regis[1], regis[2], regis[3], regis[4], regis[5]))
#------------------------------------------------------------------------------------
def insertargrupo(rango):
    for i in range(int(rango)):
        descripcion = input('Escriba la descripcion del grupo: ')
        if input('Esta seguro que desea ingresar el registro si/no: ')=='si':
          gup = ModGrupo(desc=descripcion)
          if ctrG.ingresarG(gup):
              print('Registro correcto')
          else:
              print('Error al gravar')
        else:
            ejecutarMenuG()
def modificargrupo():
    idgrup = input('Ingresa el id del grupo que desea modificar: ') 
    descripcion = input('Escriba la descripcion del grupo: ')
    if input('Esta seguro que sea modificar el registro si/no: ')=='si':
        gup= ModGrupo(desc=descripcion,ind=idgrup)
        if ctrG.modificarG(gup):
            print('Registro correcto')
        else:
            print('Error al gravar')
    else:
        ejecutarMenuG()
def eliminargrupo():
    idgrup = input('Ingresa el id del grupo que desea eliminar: ') 
    if input('Esta seguro que sea eliminar el registro si/no: ')=='si':
        gup = ModPlancuenta(ind=int(idgrup))
        if ctrG.eliminarG(gup):
          print('Registro eliminado')
        else:
          print('Error al eliminar')
    else:
        ejecutarMenuG()
def consultagrupo():
    buscar = input('Ingrese la descripcion a buscar el grupo: ')
    gup = ctrG.consultaG(buscar)
    print('\n\tId\tDescripcion')
    for regis in gup:
        print ('\n\t{}\t{}'.format(regis[0], regis[1]))

#------------------------------------------------------------------------------------

def ejecutarmenuprincipal():
    opc=''
    while True:
        opc = str(menu(['Grupos de cuentas', 'Plan de cuantas', 'Salir'],'Menu principal'))
        if opc == '0':
            print('\n<<<Grupos de cuentas>>>')
            ejecutarMenuG()
        if opc == '1':
            print('\n<<Plan de cuentas>>>')
            ejecutarMenuP()
        if opc == '2':
            print('\n<<<Gracias por usar el sistema>>>')
            input('Presione una tecla para continuar')
            break

def ejecutarMenuG():
    opc = ' '
    while True:
        opc = str(menu(['Ingresar','Modificar','Eliminar','Consultar','Salir','Regresar al menu preincipal'],'Menu grupos'))
        if opc == '0':
            print('\n<<<Ingresar datos>>>')
            valor = input('-Ingresa la cantidad de datos a insertar: ')
            insertargrupo(valor)
        if opc == '1':
            print('\n<<<Modificar datos>>>')
            modificargrupo()
        if opc == '2':
            print('\n<<<Eliminar datos>>>')
            eliminargrupo()
        if opc == '3':
            print('\n<<<Consultar datos>>>')
            consultagrupo()
        if opc == '4':
            print('\n<<<Gracias por usar el sistema>>>')
            input('Presione una tecla para continuar')
            break
        if opc == '5':
            ejecutarmenuprincipal()

def ejecutarMenuP():
    opc = ' '
    while True:
        opc = str(menu(['Ingresar','Modificar','Eliminar','Consultar','Salir','Regresar al menu preincipal'],'Menu plan cuenta'))
        if opc == '0':
            print('\n<<<Ingresar datos>>>')
            valor = input('-Ingresa la cantidad de datos a insertar: ')
            insertar(valor)
        if opc == '1':
            print('\n<<<Modificar datos>>>')
            modificar()
        if opc == '2':
            print('\n<<<Eliminar datos>>>')
            eliminar()
        if opc == '3':
            print('\n<<<Consultar datos>>>')
            consulta()
        if opc == '4':
            print('\n<<<Gracias por usar el sistema>>>')
            input('Presione una tecla para continuar')
            break
        if opc == '5':
            ejecutarmenuprincipal()

ejecutarmenuprincipal()

        




            


        

