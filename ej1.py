class NodoArbol(object):
    def __init__(self, izq=None, der=None):
        self.izq = izq
        self.der = der

    def children(self):
        return self.izq, self.der

    def __str__(self):
        return self.izq, self.der


def huffman_arbol_code(nodo, binString=''):
    '''
    Función para encontrar el codigo huffman
    '''
    if type(nodo) is str:
        return {nodo: binString}
    
    (l, r) = nodo.children()
    d = dict()
    d.update(huffman_arbol_code(l, binString + '0'))
    d.update(huffman_arbol_code(r, binString + '1'))
    return d

def huffman_arbol_decode(msg, nodo_raiz, nodo, msgd=''):
    '''
    Función para decodificar un mensaje huffman
    '''
    
    if len(msg) == 0:
        print('Mensaje decodificado: {}'.format(msgd))
        return msgd


     #print(len(msg), msgd)
    if type(nodo) is str:
        msgd = msgd + nodo
        nodo = nodo_raiz

    (l, r) = nodo.children()
    caracter = msg[0]

    if len(msg) == 1:
        msg = ''
    else:
        msg = msg[1:]

    if caracter == '1':
        huffman_arbol_decode(msg, nodo_raiz, r, msgd=msgd)
    else:
        huffman_arbol_decode(msg, nodo_raiz, l, msgd=msgd)

def crear_arbol(nodos):
    '''
    Función que crea el arbol
    :param nodos: Nodos
    :return: Nodo raíz del árbol
    '''
    print(nodos)
    print('\n')
    while len(nodos) > 1:
        (key1, c1) = nodos[0]
        (key2, c2) = nodos[1]
        nodos = nodos[2:]
        nodo = NodoArbol(key1, key2)
        nodos.append((nodo, c1 + c2))
        nodos = sorted(nodos, key=lambda x: x[1], reverse=False)
        print(nodos)
        print('\n')
    return nodos[0]

# crear la tabla de conteo como un diccionario
tabla_conteo = {
    'A':11,
    'B':2,
    'C':4,
    'D':3,
    'E':14,
    'G':3,
    'I':6,
    'L':6,
    'M':3,
    'N':6,
    'O':7,
    'P':4,
    'Q':1,
    'R':10,
    'S':4,
    'T':3,
    'U':4,
    'V':2,
    ' ':17,
    ',':2
    }
# obtener las frecuencias apartir de la tabla de conteo
total_conteo = sum(tabla_conteo.values())
tabla_frecuencia = {k:v/total_conteo for k,v in tabla_conteo.items()}
tabla_frecuencia