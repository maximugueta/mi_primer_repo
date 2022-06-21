import sys


''' genere un script que reciba por parametro 2 notas, y
si ambas son > 7 imprima aprobado, si no imprima reprobado '''

if len(sys.argv) == 3:
    nota1 = float(sys.argv[1])
    nota2 = float(sys.argv[2])

    if nota1>=7 and nota2>=7:
        print("Promocionado")
    elif nota1>=4 and nota2>=4:
        print("Aprobado")
    elif (nota1<4 or nota2<4) and (not (nota1<4 and  nota2<4)):
        if nota1<4:
            print("recupera el primer parcial")
        else:
            print("recupera el segundo parcial")
    else:
        print("desaprobo los 2 parciales")
else:
    print("Error, debe ingresar 2 notas")

    

'''
Crear un script llamado aprobado.py que realice lo siguiente:

Debe tomar 2 argumentos, ambos números enteros del 0 al 10, sino, mostrar un error.
Si ambos valores son mayores o igual a 7 devolver imprimir “Promocionado”
Si ambos valores son mayor o igual a 4 imprimir “Aprobado, debe rendir final”

'''