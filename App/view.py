"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
#from tabulate import tabulate
import traceback

""" 
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""



def new_controllers(data_types):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(data_types)
    return control
    

def set_catalog_data_type(control,datatype_to_use):
    if control['model']['datos']['size'] == 0:
        return datatype_to_use

def print_menu()->None:
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10 seleccionar el tipo de representación de la lista (ARRAY_LIST o LINKED_LIST)")
    print("0- Salir")


def load_data(control, filename:str):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    datos = controller.load_data(control,filename)
    return datos

def load_databy(control, filename:str,sort_met):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    datos = controller.load_data(control,filename)
    return datos

def rows_values(first_last_elements,headers):
    rows = []
    for dict in first_last_elements:
        for values in  dict['elements']:
            to_add = []
            for key_value in values.items():
                if key_value[0] in headers:
                    to_add.append(key_value[1])
                if len(to_add) == 11:
                    rows.append(to_add)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

# Se crea el controlador asociado a la vista

data_type = "ARRAY_LIST"
control = new_controllers(data_type)
# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = load_data(control,'DIAN/Salida_agregados_renta_juridicos_AG-small.csv')
                print("se cargaron " + str(controller.data_size(data["datos"])) + " columnas.")
                header_s = ["Año","Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
                rows = rows_values(controller.first_last_elements(data["datos"]),header_s)
                #print(tabulate(rows,header_s,tablefmt="grid",maxcolwidths= 11,maxheadercolwidths=8))
                print(controller.first_last_elements(data["datos"]))
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 10:        
                data_type = input("ingrese el tipo de dato que quiere usar. \n Ingrese 1 para ARRAY_LIST \n Ingrese 2 para LINKED_LIST \n")
                if int(data_type) == 1:
                    data_type = "ARRAY_LIST"
                elif int(data_type) == 2:
                    data_type = "SINGLE_LINKED"
                else:
                    print("Ingrese una opción válida.")
                
                small_control = new_controllers(data_type)
                print("\n ha cargado la estuctura de datos de tipo " + small_control["model"]["datos"]["type"] +" correctamente. \n" )
                muestra = input("Ingrese 1 para ingresar un tamaño de muestra para el catálogo \nIngrese 2 para ingresar el sufijo del archivo que desea cargar ((ej.: -20pct.csv, -50pct.csv, -large.csv) en el catálogo \n")
                tamanio = 0
                file_size_sufijo = None
                file_name = "DIAN/Salida_agregados_renta_juridicos_AG"
                if int(muestra) ==1:
                    tamanio = int(input("ingrese el tamaño de la meustra que desea cargar: "))
                    if tamanio < controller.data_size(data["datos"]):
                        print("\nHa cargado una muestra de "+ str(tamanio) +" datos correctamente \n")
                    else:
                        print("Ingrese una muestra válida")
                if int(muestra) == 2:
                    file_size_sufijo = input("\ningrese el sufijo del archivo que sea cargar para la muestra (ej.: -20pct.csv, -50pct.csv, -large.csv): ")
                    file_name = file_name + file_size_sufijo 
                    print("\nha cargado el archivo "+ file_name + " correctamente\n")
                else:
                    print("ingrese una opción válida")

                orden = input("Seleccione el tipo de rodenamiento que quiere utilizar; \n 1 -> Selection Sort \n 2 -> Insertion sort \n 3-> Shell sort \n")
                sort_metd = None
                if int(orden) == 1:
                    sort_metd = "Selection Sort"
                elif int(orden) == 2:
                    sort_metd = "Insertion sort"
                elif int(orden)==3: 
                    sort_metd = "Shell sort"
                else:
                    print("Ingrese una opción de Sort válida")

                data1 = load_databy(small_control, file_name,sort_metd)
                print(len(data1))
                print(type(data1))
                
            
                   
                    
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
