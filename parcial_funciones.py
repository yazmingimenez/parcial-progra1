# Lista de pacientes inicial
inventario = [
    [1234, "jorge gomez", 54, "fiebre", 2],
    [1235, "ana perez", 25, "hipotiroidismo", 5],
    [1236, "carlos lopez", 30, "neumonia", 5],
    [1237, "ludmila gonzalez", 22, "celulitis orbitaria", 10]
]

def menu()->str:
#funcion para mostrar el menu de opciones al usuario
    print("\n--- Menú de Gestión de Pacientes ---")
    print("1 - Cargar pacientes")
    print("2 - Buscar paciente por historia clinica")
    print("3 - paciente con más/menos días de internación")
    print("4 - ordenar pacientes por número de historia clínica")
    print("5 - Salir")

    return input("Ingrese una opción del 1 al 5: ")


def agregar_paciente():
#funcion para agregar un nuevo paciente , pide los datos del pacientes y los devuelve como una lista
    numero_historial = int(input("ingrese el numero de historial clinico: "))
    nombre = input("ingrese el nombre del paciente: ")
    edad = int(input("ingrese la edad del paciente: "))
    diagnosico = input("ingrese el diagnostico: ")
    dias_internacion = int(input("ingrese la cantidad de dias de internacion: "))

    return[numero_historial , nombre , edad , diagnosico , dias_internacion]


def buscar_paciente(inventario , nombre_paciente):
#funcion para buscar un paciente por su nombre , si lo encuentra lo imprime y sino muestra un mensaje de error
    for paciente in inventario:
        if paciente[1].lower() == nombre_paciente.lower(): #comparar en minisculas
            print(f"paciente encontrado: {paciente}")
            return
    print("no se encuentra paciente")


def paciente_mas_menos_dias(inventario):
#funcion para saber el paciente con mas y menos dias de internacion
    if not inventario:
        print("no hay pacientes en el inventario.")
        return
    
    paciente_mas_dias = inventario[0]  #inicializa con el primer paciente
    paciente_menos_dias = inventario[0]

    for paciente in inventario:
        if paciente[4] > paciente_mas_dias[4]: #compara dias de internacion
            paciente_mas_dias = paciente
        if paciente[4] < paciente_menos_dias[4]:
            paciente_menos_dias = paciente


    print(f"Paciente con más días de internación: {paciente_mas_dias}")
    print(f"Paciente con menos días de internación: {paciente_menos_dias}")

def ordenar_por_historial(inventario):
#funcion para ordenar el inventario de pacientes por su numero de historial clinico 
    if not inventario:
        print("No hay pacientes en el inventario.")
        return
    
    for i in range(len(inventario)):
        for j in range(0, len(inventario) - i - 1):
            if inventario[j][0] > inventario[j + 1][0]: #compara numeros de historial clinico
                inventario[j], inventario[j + 1] = inventario[j + 1], inventario[j]

    print("Pacientes ordenados por número de historial clínico: ")
    for paciente in inventario:
        numero_historial, nombre, edad, diagnostico, dias_internacion = paciente
        print(f"Número: {numero_historial} - Nombre: {nombre} - Edad: {edad} - Diagnóstico: {diagnostico} - Días de internación: {dias_internacion}")

def ordenar_por_dias(inventario):
    if not inventario:
        print("No hay pacientes en el inventario.")
        return
    
    for i in range(len(inventario)):
        for j in range(0, len(inventario) - i - 1):
            if inventario[j][4] > inventario[j + 1][4]:
                inventario[j], inventario[j + 1] = inventario[j + 1], inventario[j]

    print("Pacientes ordenados por días de internación:")

    for paciente in inventario:
        numero_historial, nombre, edad, diagnostico, dias_internacion = paciente
        print(f"Número: {numero_historial} - Nombre: {nombre} - Edad: {edad} - Diagnóstico: {diagnostico} - Días de internación: {dias_internacion}")
#bucle principal del programa
respuesta = "no"
while respuesta == "no":
    opcion = menu()  #muestra el menu y obtiene la opcion del usuario 
    
    match opcion:
        case "1":
            cantidad = int(input("cuantos pacientes desea ingresar? "))
            for _ in range(cantidad):
                paciente = agregar_paciente()  #agrega pacientes 
                inventario.append(paciente)
        
        case "2":
            if not inventario:
                print("No hay pacientes en el inventario ")
            else:
                numero_historia_clinica = int(input("Ingrese el número de historia clínica a buscar: "))
                buscar_paciente(inventario, numero_historia_clinica)

        case "3":
            paciente_mas_menos_dias(inventario) #determina el paciente con mas o menos dias de internacion

        case "4":
            ordenar_por_historial(inventario)   #ordena por numero de historial clinico
        
        case "5":
            ordenar_por_dias(inventario)  #ordena por dias de internacion

        case "6":
            respuesta = input(" usted quiere salir? : ").strip().lower() #confirma salida
            while respuesta not in ["si", "no"]:
                respuesta = input("Error. Ingrese 'si' o 'no': ").strip().lower()  #valida respuesta

        case _:
            print("Error. Ingrese una opción correcta. (De 1 a 5)") 


