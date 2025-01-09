import os
import django
from tabulate import tabulate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
django.setup()

from app1.models import Fabrica, Producto

def poblar_datos():
    # Creación de datos
    fabrica1 = Fabrica.objects.create(nombre="P&G")
    fabrica2 = Fabrica.objects.create(nombre="Colgate")

    Producto.objects.create(nombre="Ariel Suavizante", descripcion="Suavizante para la ropa", precio=1500, fabrica=fabrica1)
    Producto.objects.create(nombre="Crest Premium", descripcion="Crema dental", precio=2500, fabrica=fabrica1)
    Producto.objects.create(nombre="Downy Aroma Floral", descripcion="Ambientador de aroma floral", precio=3500, fabrica=fabrica1)

    Producto.objects.create(nombre="Protex Aloe", descripcion="Jabón de Baño", precio=1250, fabrica=fabrica2)
    Producto.objects.create(nombre="Speed Stick 24/7", descripcion="Desodorante para caballeros", precio=4500, fabrica=fabrica2)
    Producto.objects.create(nombre="Colgate 360", descripcion="Crema Dental", precio=1850, fabrica=fabrica2)

    print("Datos iniciales cargados con éxito.")

def mostrar_datos():
    # Obtener todos los registros de las tablas
    fabricas = Fabrica.objects.all()
    productos = Producto.objects.all()

    # Crear la tabla para "Fabrica"
    fabrica_data = [(fabrica.id, fabrica.nombre) for fabrica in fabricas]
    fabrica_headers = ["ID", "Nombre de la Fábrica"]

    # Crear la tabla para "Producto"
    producto_data = [(producto.id, producto.nombre, producto.descripcion, producto.precio, producto.fabrica.nombre) for producto in productos]
    producto_headers = ["ID", "Nombre del Producto", "Descripción", "Precio", "Fábrica"]

    # Mostrar las tablas
    print("\nTabla de Fabricas:")
    print(tabulate(fabrica_data, headers=fabrica_headers, tablefmt="grid"))

    print("\nTabla de Productos:")
    print(tabulate(producto_data, headers=producto_headers, tablefmt="grid"))

if __name__ == "__main__":
    poblar_datos()  # Llama a la función para poblar los datos
    mostrar_datos()  # Muestra los datos en formato tabla