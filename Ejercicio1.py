#Una Institución educativa ha recibido una donación especial que será
#repartida entre las carreras de Telecomunicaciones, Sistemas,
#Administración y Contabilidad de la siguiente forma:
#a. Telecomunicaciones 10% del valor dado a sistemas
#b. Sistemas: 25% del valor dado a Administración
#c. Administración: 35% del valor de la donación
#d. Contabilidad: lo que resta de la donación

Donacion = float(input("Ingrese el monto de la donacion: "))
Porcentaje_telecomunicaciones = Donacion * 0.10
Porcentaje_Sistemas = Donacion * 0.25
Porcentaje_administracion = Donacion * 0.35
sumaPorcentajes = Porcentaje_telecomunicaciones + Porcentaje_Sistemas + Porcentaje_administracion

contabilidad = Donacion - sumaPorcentajes;

print(f"Le corresponde a telecomunicacion ${Porcentaje_telecomunicaciones:,}")
print(f"Le corresponde a sistemas ${Porcentaje_Sistemas:,}")
print(f"Le corresponde a administracion ${Porcentaje_administracion:,}")
print(f"Le corresponde a contabilidad ${contabilidad:,}")