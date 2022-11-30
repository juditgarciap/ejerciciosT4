def biseccion(f, a, b, tol, iteracion=1):
    # Se pretende aproximar la raíz x de la función f(x),
    # que se encuentra en el intervalo [a,b],
    # con una tolerancia |f(x)| < tol.
    
    # Primero comprobar si en el intervalo [a,b] existe una raíz.
    if f(a)*f(b) >= 0:
        # La existencia de una raíz f(x) = 0 implica que,
        # al evaluar la función por ambos extremos f(a) y f(b),
        # se deben obtener signos diferentes, esto es f(a)*f(b) < 0.
        print("En el intervalo especificado no existe raíz para la función.")
     

    # Paso de la bisección: Dividir el intervalo en un punto medio.
    x = (a + b)/2
    
    # Finalizar si se cumple la tolerancia,
    # y por lo tanto retornar la raíz estimada y el número de iteraciones.
    if -tol < f(x) < tol:
        return x, iteracion
    
    # Preguntar si x es una mejora del intervalo por la izquierda f(a),
    # esto es, si f(x) no cambia de signo con respecto a f(a). 
    elif f(a)*f(x) >= 0:
     # Actualizar intervalo y realizar llamada recursiva de la función.
        return biseccion(f, x, b, tol, iteracion+1)
    # Preguntar si x es una mejora del intervalo por la derecha f(b),
    # esto es, si f(x) no cambia de signo con respecto a f(b). 
    elif f(b)*f(x) >= 0:
        # Actualizar intervalo y realizar llamada recursiva de la función.
        return biseccion(f, a, x, tol, iteracion+1)



# Ejecutar pruebas con la función objetivo, para una tolerancia de 0.001:    
f = lambda x: x**3 + x + 16
x, iteraciones = biseccion(f, -4, 0, 1e-3)
print("Raíz estimada por método de la bisección:", x)
print("N° de iteraciones:", iteraciones)


# https://es.wikipedia.org/wiki/M%C3%A9todo_de_bisecci%C3%B3n




# Método de Newton-Raphson de una función f(x)

def newton_raphson(f, x0, tol, iteracion=1):
    # Se pretende aproximar la raíz x de la función f(x),
    # que se encuentra cercana al valor x0,
    # con una tolerancia |f(x)| < tol.
        
    # Paso de Newton-Raphson: Encontrar una mejor aproximación para x,
    # con base en la derivada de f(x0). 
    dfx0 = (f(x0 + tol/2) - f(x0 - tol/2)) / tol
    # Para estimar df(x0) vemos que puede aprovecharse el valor de tolerancia,
    # el cual se toma como el h o delta x de la formula de derivación.
    x = x0 - f(x0)/dfx0

    
    # Finalizar si se cumple la tolerancia,
    # y por lo tanto retornar la raíz estimada y el número de iteraciones.
    if -tol < f(x) < tol:
        return x, iteracion
    
    # Actualizar aproximación para x,
    # y realizar llamada recursiva de la función.
    return newton_raphson(f, x, tol, iteracion+1)
