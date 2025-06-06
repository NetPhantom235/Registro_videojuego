videojuegos=[]
plataformas=("ps5", "PC", "xbox series x", "nintendo switch")

menu="""
##### Menu de Videojuegos ######

1. Registrar videojuego
2. Ver videojuego
3. Modificar videojuego
4. Eliminar
5. Salir
"""

while True:
    print("="*50)
    print(menu.center(200 ,"="))
    print("="*50)
    option=(input("ingresa una opcion (1-5): "))
    if option=="1":
        codigo=int(input("Ingresa el codigo del videojuego: "))
        nombre= (input("ingresa el nombre del juego"))
        genero=(input("ingresa el genero del videojuego: "))
        print("\nPlataformas disponibles: ")
        print("1. ps5") 
        print("2. PC") 
        print("3. xbox series x")
        print("4. nintendo switch")
        plataforma_codigo=int(input("Seleccione el numero de la plataforma: "))
        plataforma=plataformas[plataforma_codigo - 1]
        videojuegos={
            "codigo":codigo,
            "nombre":nombre,
            "genero":genero,
            "plataforma":plataforma
        }
        videojuegos.append(videojuegos)
        print("Videojuego registrado con exito!")
    elif option=="2":
        pass
    elif option=="3":
        pass
    elif option=="4":
        pass
    elif option=="5":
        print("saliendo del programa.")
        break
    else:
        print("opcion invalida")