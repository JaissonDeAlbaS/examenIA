#Un alumno desea saber cuál será su calificación final en la materia de
# fundamentos de programación. Dicha calificación se compone de los
# siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
# calificación de un examen en clase y 20% de la calificación de un proyecto
# final.


calificacion_taller_1 = float(input("Calificacion taller 1: "))
calificacion_taller_2 = float(input("Calificacion taller 2: "))
calificacion_taller_3 = float(input("Calificacion taller 3: "))
calificacion_examen = float(input("Calificacion examen: "))
calificacion_proyecto_final = float(input("Calificacion proyecto final: "))

suma_talleres = calificacion_taller_1 + calificacion_taller_2 + calificacion_taller_3
promedio_talleres = suma_talleres/3

nota1 = promedio_talleres * 0.50
nota2 = calificacion_examen * 0.30
nota3 = calificacion_proyecto_final * 0.20

sumatoria_notas = nota1 + nota2 + nota3

print(f"Promedio de los 3 talleres: {promedio_talleres:,}")
print(f"nota 50%: {nota1:,}")
print(f"nota 30% {nota2:,}")
print(f"nota 20% {nota3:,}")
print(f"Calificacion final de fundamentos de programación de : {sumatoria_notas:,}")
