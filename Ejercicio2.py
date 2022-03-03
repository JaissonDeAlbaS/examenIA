#Haga un programa en Python que permita ingresar el dinero invertido por
#tres personas para formar una empresa. Cada una de ellas invierte una
#cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
#al total de la inversión.

persona1 = float(input("Ingrese el dinero invertido persona 1: "))
persona2 = float(input("Ingrese el dinero invertido persona 2: "))
persona3 = float(input("Ingrese el dinero invertido persona 3: "))
total_invertido = persona1 + persona2 + persona3

#10*100/10.000
porcentaje_persona1 = (persona1 * 100)/total_invertido
porcentaje_persona2 = (persona2 * 100)/total_invertido
porcentaje_persona3 = (persona3 * 100)/total_invertido

print(f"Persona 1 invirtio: ${persona1:,} que corresponde al {porcentaje_persona1:,}%")
print(f"Persona 2 invirtio: ${persona2:,} que corresponde al {porcentaje_persona2:,}%")
print(f"Persona 3 invirtio: {persona3:,} que corresponde al {porcentaje_persona3:,}%")