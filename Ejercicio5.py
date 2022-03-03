#Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el porcentaje de alumnos de cada uno de los cursos.

cantidad_alumnos_redes = int(input("Ingrese la cantidad de alumnos de redes: "))
cantidad_alumnos_contabilidad = int(input("Ingrese la cantidad de alumnos de contabilidad: "))
cantidad_alumnos_diseño = int(input("Ingrese la cantidad de alumnos de diseño: "))
cantidad_total_alumnos = cantidad_alumnos_redes + cantidad_alumnos_contabilidad + cantidad_alumnos_diseño

porcentaje_redes =  (cantidad_alumnos_redes * 100)/cantidad_total_alumnos
porcentaje_contabilidad =  (cantidad_alumnos_contabilidad * 100)/cantidad_total_alumnos
cantidad_alumnos_diseño =  (cantidad_alumnos_diseño * 100)/cantidad_total_alumnos

print(f"Redes: {porcentaje_redes:,}%")
print(f"Contabilidad: {porcentaje_contabilidad:,}%")
print(f"Diseño: {cantidad_alumnos_diseño:,}%")