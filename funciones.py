# aquí iremos agregando todas las funciones del sistemasdef mostrar_productos(productos, inventario):
def mostrar_productos(productos, inventario):
    for codigo in productos:

        print(f"\nCODIGO: {codigo}")
        print("--------------------------")
        print(f"Nombre: {productos[codigo][0]}")
        print(f"Categoría: {productos[codigo][1]}")
        print(f"Precio: ${productos[codigo][2]}")
        print(f"Disponible: {productos[codigo][3]}")
        print(f"Stock: {inventario[codigo][0]}")
        print(f"Vendidos: {inventario[codigo][1]}")
        print("--------------------------")

def buscar_codigo(codigo, productos):

    codigo = codigo.upper()

    for c in productos:
        if c.upper() == codigo:
            return True

    return False

def actualizar_precio(codigo, nuevo_precio, productos):

    if buscar_codigo(codigo, productos):

        codigo = codigo.upper()

        productos[codigo][2] = nuevo_precio

        return True

    return False