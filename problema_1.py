# Importamos tiempo para el calculo de los tiempos de ejecucion
import time


# Problrma 1 
# Autor: Jesús Haans Lopez Hernandez
# sea S = S0, S1, s2, ..., Sn+2 
# donde: 
# Sn+2 =3(Sn+1) + 2Sn

# Veremos diferentes formas de resolverlo
# asi como el tiempo que toca ejecutarlos
# aun que en la practica lo que mediremos 
# son las operaciones aritmeticas para medir 
# la complejidad de la funcion.

# Solucion recursiva.
# Desventajas de esta solucion no es muy eficiente ya que tarda mucho tiempo.

def solrec(n):
    if n < 2:
        return n
    else:
        return 3*solrec(n-1) + 2*solrec(n-2)

# solucion recursiva mejorada.
# tarda un poco menos pero es muy mal eficiente en terminos de memoria.

def solrec2(n):
    if n == 1:
        return (1,0)
    else:
        (p,pp)=solrec2(n-1)
        return (3*p+2*pp,p)


# Solucion iterativa.
# Es la solucion definitiva para el problema 1.

def soliter(n):
    i=1
    vi=1
    vp=0
    while i<n:
        i += 1
        backup = vp
        vp=vi
        vi=3*vi+2*backup
    return vi

# Funcion para medir la complejidad de la funcion en tiempo no es 
# muy efectivo dado que si cambiamos de maquina o de implentacion de python
# el tiempo de ejecucion puede variar y es por eso que siempre nos fijamos
# en la complejidad en terminos de operaciones aritmeticas.

def time_problem(n):
    print("Solucion recursiva:")
    start = time.process_time() 
    print(solrec(n))
    end = time.process_time()
    print("tomo un tiempo de " + str(end - start))
    print("Solucion recursiva mejorada:")
    start = time.process_time()
    print(solrec2(n))
    end = time.process_time()
    print("tomo un tiempo de " + str(end - start))
    print("Solucion iterativa:")
    start=time.process_time()
    print(soliter(n))
    end=time.process_time()
    print("tomo un tiempo de " + str(end - start))


# Ejecucion del programa

print("Solucion del problema 1 \n")
print("Ingresa un n :\n")
n = int(input())
time_problem(n)