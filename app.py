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
        pass
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