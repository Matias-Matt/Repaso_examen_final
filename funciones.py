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

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True

def validar_categoria(categoria):
    if categoria.strip() == "":
        return False
    return True

def validar_precio(precio):
    if precio > 0:
        return True
    return False

def validar_stock(stock):
    if stock >= 0:
        return True
    return False

def validar_vendidos(vendidos):
    if vendidos >= 0:
        return True
    return False

def validar_disponible(opcion):
    opcion = opcion.lower()
    if opcion == "s":
        return True
    if opcion == "n":
        return True
    return False

def validar_codigo(codigo, productos):
    if codigo.strip() == "":
        return False
    if buscar_codigo(codigo, productos):
        return False
    return True

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):

    if buscar_codigo(codigo, productos):
        return False
    if disponible.lower() == "s":
        disponible = True
    else:
        disponible = False
    productos[codigo] = [
        nombre,
        categoria,
        precio,
        disponible
    ]
    inventario[codigo] = [
        stock,
        vendidos
    ]
    return True

def eliminar_producto(codigo, productos, inventario):
    if buscar_codigo(codigo, productos):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False

def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total_stock += inventario[codigo][0]
    print(f"Stock total de {categoria}: {total_stock}")
    

def buscar_precio(precio_min, precio_max, productos, inventario):
    lista = []
    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]
        if precio >= precio_min and precio <= precio_max and stock > 0:
            lista.append((productos[codigo][0], codigo))
    lista.sort()
    for nombre, codigo in lista:
        print(f"{nombre} -- {codigo}")
        
def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 7:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

