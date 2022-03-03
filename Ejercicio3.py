#Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
#ventas efectuadas en el mes. 
#El vendedor desea saber cuanto dinero en total obtendrá por las ventas que realiza en el mes. 
#Desarrolle un programa en Python que permita mostrar el valor ganado por comisión y el valor total a pagar al vendedor.


sueldo_base = float(input("Ingrese el sueldo base: "))
total_ventas = float(input("Ingrese el valor total de las ventas realizadas en el mes : "))
valor_total_comision = total_ventas * 0.15
Valor_total_pago = sueldo_base + valor_total_comision

print(f"El valor total de la comisión es: ${valor_total_comision:,}")
print(f"El valor total a pagarle al vendedor es: ${Valor_total_pago:,}")