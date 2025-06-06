videojuegos = []
plataformas = ("ps5", "PC", "xbox series x", "nintendo switch")

menu = """
##### Menu de Videojuegos ######

1. Registrar videojuego
2. Ver videojuego
3. Modificar videojuego
4. Eliminar
5. Salir
"""

while True:
    print("=" * 50)
    print(menu.center(200, "="))
    print("=" * 50)
    option = input("Ingresa una opción (1-5): ")

    if option == "1":
        try:
            codigo = int(input("Ingresa el código del videojuego: "))
            nombre = input("Ingresa el nombre del juego: ").strip()
            genero = input("Ingresa el género del videojuego: ").strip()
            
            if not nombre or not genero:
                print("El nombre y género no pueden estar vacíos.")
                continue

            print("\nPlataformas disponibles: ")
            print("1. ps5") 
            print("2. PC") 
            print("3. xbox series x")
            print("4. nintendo switch")

            plataforma_codigo = int(input("Seleccione el número de la plataforma: "))
            if plataforma_codigo < 1 or plataforma_codigo > 4:
                print("Plataforma inválida.")
                continue

            plataforma = plataformas[plataforma_codigo - 1]
            videojuego = {
                "codigo": codigo,
                "nombre": nombre,
                "genero": genero,
                "plataforma": plataforma
            }
            videojuegos.append(videojuego)
            print("Videojuego registrado con éxito!")

        except ValueError:
            print("Error: Debes ingresar un número válido.")

    elif option == "2":
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados!")
        else:
            print("\n--- LISTA DE VIDEOJUEGOS ---")
            for v in videojuegos:
                print(f"Código: {v['codigo']}, Nombre: {v['nombre']}, Género: {v['genero']}, Plataforma: {v['plataforma']}")

    elif option == "3":
        try:
            codigo_buscar = int(input("Ingrese el código del videojuego a modificar: "))
            encontrado = False
            for v in videojuegos:
                if v["codigo"] == codigo_buscar:
                    v["nombre"] = input("Nuevo nombre: ").strip()
                    v["genero"] = input("Nuevo género: ").strip()

                    print("\nPlataformas disponibles: ")
                    print("1. ps5") 
                    print("2. PC") 
                    print("3. xbox series x")
                    print("4. nintendo switch")

                    plataforma_codigo = int(input("Seleccione el número de la plataforma: "))
                    if plataforma_codigo < 1 or plataforma_codigo > 4:
                        print("Plataforma inválida.")
                        break

                    v["plataforma"] = plataformas[plataforma_codigo - 1]
                    print("Videojuego modificado con éxito!")
                    encontrado = True
                    break

            if not encontrado:
                print("Videojuego no encontrado!")

        except ValueError:
            print("Error: Debes ingresar un número válido.")

    elif option == "4":
        try:
            codigo_eliminar = int(input("Ingrese el código del videojuego a eliminar: "))
            eliminado = False
            for v in videojuegos:
                if v["codigo"] == codigo_eliminar:
                    videojuegos.remove(v)
                    print("Videojuego eliminado con éxito!")
                    eliminado = True
                    break
            if not eliminado:
                print("Videojuego no encontrado!")
        except ValueError:
            print("Error: Debes ingresar un número válido.")

    elif option == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida.")
