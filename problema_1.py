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


def solrec(n):
    if n < 2:
        return n
    else:
        return 3*solrec(n-1) + 2*solrec(n-2)