### 1.Sintaxis básica: Python utiliza la indentación para definir bloques de código, a diferencia de otros lenguajes que usan llaves o paréntesis. 
## La indentación correcta es crucial, ya que define la estructura del programa.
## Un error común es mezclar espacios y tabulaciones, lo que puede llevar a errores.

# Ejemplo con: Edad insertada por el usuario
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Entrada con descuento")  # Si es menor de 18
else:
    print("Entrada general")  # Si tiene 18 o más

## En este ejemplo, las líneas print(...) están indentadas cuatro espacios para indicar que pertenecen a los bloques if y else.
  


### 2.Tipos de datos: Necesitaré trabajar con diferentes tipos de datos como:

## a) Enteros (int) para representar números enteros como la cantidad de entradas o el número de sala.

# Ejemplo: Cantidad de entradas
cantidad_entradas = 5

# Ejemplo: Número de sala
numero_sala = 2

print(f"Cantidad de entradas: {cantidad_entradas}")
print(f"Número de sala: {numero_sala}")

## b) Flotantes (float) para representar números con decimales como el precio de una entrada.

# Ejemplo: Precio de una entrada
precio_entrada = 12.50

# Ejemplo: Descuento aplicado
descuento = 2.75

print(f"Precio de la entrada: {precio_entrada}")
print(f"Descuento aplicado: {descuento}")

## c) Cadenas (str) para representar texto como el nombre de una película o el tipo de entrada.

# Ejemplo:Nombre de una película
nombre_pelicula = "Inception"

# Tipo de entrada
tipo_entrada = "VIP"

print(f"Nombre de la película: {nombre_pelicula}")
print(f"Tipo de entrada: {tipo_entrada}")

## d) Boleanos (bool) para representar valores de verdad (True o False), que serán útiles para las condiciones de las tarifas especiales.

# Ejemplo: Tarifa especial aplicada
tarifa_especial = True

# Ejemplo: Entrada agotada
entrada_agotada = False

print(f"Tarifa especial aplicada: {tarifa_especial}")
print(f"Entrada agotada: {entrada_agotada}")



### 3.Variables: Una variable es un nombre que se le asigna a un valor en la memoria. En Python, las variables se declaran simplemente asignándoles un valor.

nombre_pelicula = "Avengers: Endgame"
precio_entrada = 10.50
print(f"Película: {nombre_pelicula}")
print(f"Precio de la entrada: {precio_entrada}")

# En este ejemplo, nombre_pelicula es una variable que almacena una cadena y precio_entrada una variable que almacena un flotante.



### 4.Operadores: Aprenderás a usar operadores para realizar operaciones con los datos:

## Aritméticos: +, -, *, /, // (división entera), % (módulo) y ** (potenciación) para realizar cálculos matemáticos.

# Tipos de datos numéricos
entero = 10  # int
flotante = 3.14  # float
print("Entero:", entero)
print("Flotante:", flotante)

# Tipos de datos de texto
cadena = "Hola, mundo!"  # str
print("Cadena:", cadena)

# Operadores aritméticos
suma = 5 + 2
resta = 10 - 3
multiplicacion = 4 * 6
division = 15 / 4
division_entera = 15 // 4
modulo = 17 % 5
potencia = 2 ** 3
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División Entera:", division_entera)
print("Módulo:", modulo)  # El operador módulo (%) devuelve el resto de una división entera. [1]
print("Potencia:", potencia)

# Operaciones con precios
a = 5
b = 3

print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")

# Calcular precio promedio de dos entradas
precio_entrada1 = 12.50
precio_entrada2 = 10.75

precio_promedio = (precio_entrada1 + precio_entrada2) / 2
print(f"Precio promedio de las entradas: {precio_promedio}")

# Calcular cuántos combos completos de palomitas y refrescos se pueden vender
total_comida = 35  # unidades disponibles
combo = 3  # unidades por combo

combos_completos = total_comida // combo
print(f"Combos completos disponibles: {combos_completos}")

# Calcular unidades de comida sobrantes después de formar combos
total_comida = 35  # unidades disponibles
combo = 3  # unidades por combo

sobrantes = total_comida % combo
print(f"Unidades de comida sobrantes: {sobrantes}")

# Calcular la potencia de aumento en precio de entradas después de varias subidas
precio_inicial = 10
incremento_potencia = 2  # Factor de multiplicación cada vez

precio_final = precio_inicial * (2 ** incremento_potencia)
print(f"El precio final después de dos aumentos es: {precio_final}")


## Comparación: ==, !=, >, <, >= y <= para comparar valores.

# Igual a (==)
a = 18
b = 15
resultado = (a == b)  # resultado es False
print(f"{a} == {b}: {resultado}")

# Mayor que (>)
a = 18
b = 15
resultado = (a > b)  # resultado es True
print(f"{a} > {b}: {resultado}")

# Menor o igual que (<=)
a = 18
b = 15
resultado = (a <= b)  # resultado es True
print(f"{a} <= {b}: {resultado}")


## Lógicos: and, or y not para combinar condiciones.

# AND (and)
a = True
b = False
resultado = a and b  # resultado es False
print(f"{a} and {b}: {resultado}")

# OR (or)
a = True
b = False
resultado = a or b  # resultado es True
print(f"{a} or {b}: {resultado}")

# NOT (not)
a = True
resultado = not a  # resultado es False
print(f"not {a}: {resultado}")

# Estos son ejemplos básicos de operadores aritméticos, de comparación y lógicos en Python.



### 5. Estructuras de Control

# Sentencia if-else
# Determinar si hay promoción
promocion = True

if promocion:
    print("Promoción aplicada: 2x1 en entradas")
else:
    print("No hay promoción disponible")

# Bucle for
# Mostrar horarios de función
horarios = [14, 16, 18, 20]
for horario in horarios:
    print(f"Función disponible a las {horario}:00")

# Bucle while
# Contar boletos vendidos
boletos_vendidos = 0
meta = 5

while boletos_vendidos < meta:
    boletos_vendidos += 1
    print(f"Boletos vendidos: {boletos_vendidos}")



### 6. Funciones

# Función para calcular precio total
def calcular_precio_total(precio, cantidad):
    return precio * cantidad

precio_entrada = 10.50
cantidad = 3

print(f"El precio total es: {calcular_precio_total(precio_entrada, cantidad)}")


### 7. Clases y Objetos

# Clase Película
class Pelicula:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def mostrar_info(self):
        print(f"Película: {self.nombre}, Género: {self.genero}")

# Crear instancia
mi_pelicula = Pelicula("Interstellar", "Ciencia Ficción")
mi_pelicula.mostrar_info()


### 8. Módulos

# Calcular redondeo de precios
import math

precio_original = 12.75
precio_redondeado = math.ceil(precio_original)

print(f"Precio original: {precio_original}, Precio redondeado: {precio_redondeado}")