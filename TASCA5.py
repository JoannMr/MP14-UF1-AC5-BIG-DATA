# TAREA 2
# a)Usa la función map() para crear una lista de números cuyos elementos sean el doble de los elementos de otra lista.

lista_original = [1, 2, 3, 4, 5]

lista_doble = list(map(lambda x: x * 2, lista_original))

print(lista_doble)

# b)Usa la función map() para crear una lista que convierta a mayúsculas todas las palabras de otra lista.

palabras = ["garza", "urraca", "gorrión", "petirrojo"]

palabras_mayusculas = list(map(lambda x: x.upper(), palabras))

print(palabras_mayusculas)

# TAREA 3

# a)Crea una tupla a partir de una lista. Usa la función constructora de tuplas.

lista_original = [1, 2, 3, 4, 5]

tupla_resultante = tuple(lista_original)

print(tupla_resultante)

# b) Crea una lista a partir de una tupla. Usa la función constructora de listas.

tupla_original = (10, 20, 30, 40, 50)

lista_resultante = list(tupla_original)

print(lista_resultante)

# c)Crea tres listas de dos elementos cada una y luego crea una tupla llamada x que las contenga (es decir, algo del estilo: ([1,2], [3,4], [8,2]).

lista1 = [1, 2]
lista2 = [3, 4]
lista3 = [8, 2]

tupla_x = (lista1, lista2, lista3)

print(tupla_x)

# d)Prueba a modificar la posición 0 de la lista que ocupa la posición 0 de la tupla, con:

tupla_x[0][0] = 100

print(tupla_x)

# ¿Has podido realizar la modificación? ¿Cómo es posible, si las tuplas son inmodificables?

Aunque las tuplas son inmutables, si contienen elementos mutables como listas, estos elementos pueden modificarse. La inmutabilidad de la tupla se refiere a la imposibilidad de agregar o quitar elementos directamente, pero los elementos mutables internos pueden cambiar.

# TAREA 4

cola_pedidos = []

# a) Función para procesar el primer pedido de la cola

def procesarPedido():
    if cola_pedidos:
        pedido = cola_pedidos.pop(0)
        print(f"Procesando {pedido}....")
    else:
        print("La cola de pedidos está vacía.")

# b)Una función encolarPedido que añada un pedido al final de la lista.

def encolarPedido(pedido):
    cola_pedidos.append(pedido)
    print(f"Pedido {pedido} añadido a la cola.")

# c)Una función vaciarCola que elimine todos los pedidos de la lista.

def vaciarCola():
    cola_pedidos.clear()
    print("La cola de pedidos ha sido vaciada.")

# d)Con listas podemos representar, además de colas, también pilas. Investiga cuál es la diferencia entre una cola (queue) y una pila (stack). ¿Cómo cambiarían las funciones anteriores si en lugar de atender una cola, atendieran una pila?

Cola; El primer elemento que entra es el primero en salir. 
Pila; El último elemento que entra es el primero en salir.

# Seria;

def procesarPedidoPila():
    if cola_pedidos:
        pedido = cola_pedidos.pop()
        print(f"Procesando {pedido}....")
    else:
        print("La pila de pedidos está vacía.")

def encolarPedidoPila(pedido):
    cola_pedidos.append(pedido)
    print(f"Pedido {pedido} añadido a la pila.")

def vaciarPila():
    cola_pedidos.clear()
    print("La pila de pedidos ha sido vaciada.")

# TAREA 5 

dicc_prefijos = {
    "91": "Comunidad de Madrid",
    "93": "Cataluña",
    "95": "Andalucía",
}

def gestionarPrefijos():
    opcion = input("¿Deseas consultar (c) o agregar (a) un prefijo? ").lower()

    if opcion == "c":
        prefijo_consulta = input("Introduce el prefijo a consultar: ")
        comunidad = dicc_prefijos.get(prefijo_consulta, "Prefijo no encontrado.")
        print(f"El prefijo {prefijo_consulta} pertenece a la comunidad autónoma de {comunidad}.")
    elif opcion == "a":
        nuevo_prefijo = input("Introduce el nuevo prefijo: ")
        nueva_comunidad = input("Introduce la comunidad autónoma asociada: ")
        dicc_prefijos[nuevo_prefijo] = nueva_comunidad
        print(f"Prefijo {nuevo_prefijo} añadido para la comunidad autónoma de {nueva_comunidad}.")
    else:
        print("Opción no válida. Por favor, elige 'c' o 'a'.")

gestionarPrefijos()

# TAREA 6

# a)Pida al usuario una cadena de texto de cualquier número de palabras; 

cadena_texto = input("Introduce una cadena de texto: ")

# b)Cuente las ocurrencias de cada palabras que hay en esa cadena (utiliza el método split para separar palabras); 

palabras = cadena_texto.split()

# c)Que vaya almacenando la información en un diccionario; 

diccionario_ocurrencias = {}
for palabra in palabras:
    diccionario_ocurrencias[palabra] = diccionario_ocurrencias.get(palabra, 0) + 1

# d)Printe el diccionario por pantalla.

print("Diccionario de ocurrencias:")
for palabra, ocurrencias in diccionario_ocurrencias.items():
    print(f"{palabra}: {ocurrencias}")

