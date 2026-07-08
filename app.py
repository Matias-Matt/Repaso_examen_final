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

print(validar_nombre("Cuaderno"))
print(validar_nombre(""))

print(validar_precio(100))
print(validar_precio(-5))