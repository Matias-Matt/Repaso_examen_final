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

print(buscar_codigo("P101", productos))
print(buscar_codigo("p101", productos))
print(buscar_codigo("P999", productos))

print(actualizar_precio("P101", 3500, productos))

mostrar_productos(productos, inventario)