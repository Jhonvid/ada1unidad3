class Pila:
    def __init__(self):
        # La pila se almacena en una lista
        self.items = []

    def esta_vacia(self):
        # Retorna True si la pila está vacía
        return len(self.items) == 0

    def apilar(self, item):
        # Agrega un elemento a la pila
        self.items.append(item)

    def desapilar(self):
        # Elimina y retorna el elemento en el tope de la pila (si no está vacía)
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La pila está vacía"

    def ver_tope(self):
        # Retorna el elemento en el tope de la pila sin eliminarlo
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"

    def tamano(self):
        # Retorna el tamaño de la pila
        return len(self.items)

# Ejemplo de uso de la clase Pila
mi_pila = Pila()

# Agregar elementos
mi_pila.apilar(10)
mi_pila.apilar(20)
mi_pila.apilar(30)

print("Elemento en el tope:", mi_pila.ver_tope())  # Salida: 30
print("Tamaño de la pila:", mi_pila.tamano())     # Salida: 3

# Eliminar el tope de la pila
print("Elemento desapilado:", mi_pila.desapilar()) # Salida: 30
print("Elemento en el tope:", mi_pila.ver_tope())  # Salida: 20

# Verificar si la pila está vacía
print("¿La pila está vacía?", mi_pila.esta_vacia())  # Salida: False

# Vaciar la pila
mi_pila.desapilar()
mi_pila.desapilar()

# Intentar desapilar de una pila vacía
print("Elemento desapilado:", mi_pila.desapilar())  # Salida: La pila está vacía
