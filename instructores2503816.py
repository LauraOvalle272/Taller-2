instructores2503816 = {}
while True:
    print("Instructores")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("¿Qué opción deseas realizar?: "))
    if opcion == 1:
        nombre = input("Nombre del instructor: ")  
        if nombre in instructores2503816:
            print( "%s ya existe y la materia que dicta es %s " % (nombre,instructores2503816[nombre]))
            print("su telefono es ", telefono)
        else:
            telefono = input("Dame el telefono del instructor: ")
            instructores2503816[nombre]=telefono
            materia = input("Ingrese la materia que dicta: ")
            instructores2503816[nombre]=materia
    elif opcion == 2:
        texto = input("Nombre del instructor a buscar:")
        print("Se encontraron los siguientes resultados:")   
        if nombre in instructores2503816:
            print( "%s es la instroctura que dicta la materia %s " % (nombre,instructores2503816[nombre]))
            print("su telefono es ", telefono) 
    elif opcion == 3:
        nombre = input("Nombre del instructor a eliminar:")    
        if nombre in instructores2503816:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del instructores2503816[nombre]
        else:
                print("No existe el instructor indicado")
    elif opcion == 4:
            print(nombre,"->",telefono,"->", materia )
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
