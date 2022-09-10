# Calculadora con menú 

from math import log
from pickle import FALSE

print("----------------------------------------")
print("--------- CALCULADORA ----- MENU -------")

# Input
bandera = False
x = float(input("Ingrese el valor del número x: "))
y = float(input("Ingrese el valor del número y: "))

print("\nEscoje la operación que desea realizar: \n")
# Se despliega el menú para seleccionar la operación que deseas realizar:
print("1. Sumar(El primero más el segundo)")
print("2. Restar(El primero menos el segundo)")
print("3. Multiplicar(El primero por el segundo)")
print("4. Dividir(El primero sobre el segundo)")
print("5. Potencia(El primero a la potencia del segundo)")
print("6. Logaritmo(El logaritmo del primero)")

opcion = int(input("\nEscoge la opción: "))
