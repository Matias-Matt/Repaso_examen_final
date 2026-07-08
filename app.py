from funciones import *

productos = {
    "P101": ["Cuaderno", "Papelería", 2490, True],
    "P102": ["lápiz", "Papelería", 590, True],
    "P103": ["botella", "accesorio", 6990, False],
    "P104": ["mochila", "accesorio", 24990, True]
}

inventario = {
    "P101": [30, 15],
    "P102": [120, 50],
    "P103": [0, 10],
    "P104": [8, 25]
}

while True:

    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Mostrar productos")
    print("7. Salir")
    print("====================================")
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese la categoría: ")
        stock_categoria(categoria, productos, inventario)
        
    elif opcion == 2:
        while True:
            try:
                minimo = int(input("Ingrese precio mínimo: "))
                maximo = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar números enteros.")
        buscar_precio(minimo, maximo, productos, inventario)
        
    elif opcion == 3:
        while True:
            codigo = input("Ingrese código: ").upper()
            try:
                nuevo_precio = int(input("Nuevo precio: "))
                if actualizar_precio(codigo, nuevo_precio, productos):
                    print("Precio actualizado.")
                else:
                    print("Código inexistente.")
            except ValueError:
                print("Precio inválido.")
            continuar = input("¿Desea continuar? (s/n): ")
            if continuar.lower() != "s":
                break
            
    elif opcion == 4:
        codigo = input("Código: ").upper()
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        while True:
            try:
                precio = int(input("Precio: "))
                break
            except ValueError:
                print("Precio inválido.")
        disponible = input("Disponible (s/n): ")
        while True:
            try:
                stock = int(input("Stock: "))
                vendidos = int(input("Vendidos: "))
                break
            except ValueError:
                print("Debe ingresar números.")
        if agregar_producto(codigo, nombre, categoria, precio,
                            disponible, stock, vendidos,
                            productos, inventario):
            print("Producto agregado correctamente.")
        else:
            print("El código ya existe.")
            
    elif opcion == 5:
        codigo = input("Ingrese código: ").upper()
        if eliminar_producto(codigo, productos, inventario):
            print("Producto eliminado.")
        else:
            print("Código inexistente.")
            
    elif opcion == 6:
        mostrar_productos(productos, inventario)
        
    elif opcion == 7:
        print("Programa finalizado.")
        break