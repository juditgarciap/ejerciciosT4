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
     