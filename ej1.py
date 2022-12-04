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