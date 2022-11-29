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
    