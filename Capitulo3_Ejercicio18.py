print("Ingrese Codigo")
codigo=str(input())
print("Ingrese Nombre")
nombre=str(input())
print("Ingrese la cantidad de horas trabajadas en el mes")
horas_trabajo_mes=int(input())
print("Ingrese el pago por hora")
pago_hora=float(input())
print("Ingrese el porcentaje de retencion en la fuente")
porcentaje_retencion=float(input())
salario_bruto=horas_trabajo_mes*pago_hora
retencion_fuente=salario_bruto*(porcentaje_retencion/100)
salario_neto=salario_bruto - retencion_fuente
print("Codigo:", codigo)
print("Nombre:", nombre)
print("salario bruto:", salario_bruto)
print("salario neto:", salario_neto)
