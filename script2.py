import sys

#print(f"hola {sys.argv[1]}")

#realizar un script que imprima una palabra una cantida de veces pasada por parametro

#imprimir hola 5

if len(sys.argv) != 3:
    print("error, necesito 2 argumentos")
else:
    for i in range (int(sys.argv[2])):
        print(sys.argv[1])
