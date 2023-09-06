TIME_STEP = 0.1

def generadorDeFuncion(vx: float, vy: float, g: float, h: float):
    """Genera una función para describir la posición de un objeto usando las fórmulas del tiro parabólicos
    
    Parametros
    ----------
    vx : float
        La velocidad horizontal en (m/s)
    vy : float
        La velocidad vertical en (m/s)
    g : float
        La aceleración de la gravedad en (m/s^2)
    h : float
        La altura en (m)
    """

    def funcionGenerada(t: float) -> tuple[float,float]:

        x = vx * t
        y = -g*t**2 + vy*t + h

        return x,y
    
    return funcionGenerada
    

if __name__ == "__main__":
    # Pedimos al usuario los parámetros
    vx: float = float(input("Ingrese la velocidad en x (m/s): "))
    vy: float = float(input("Ingrese la velocidad en y (m/s): "))
    g: float = float(input("Ingrese la aceleración de la gravedad (m/s^2): "))
    h: float = float(input("Ingrese la altura (m): "))

    #Creamos la función en función del tiempo para las posiciones
    funcion = generadorDeFuncion(vx,vy,g,h)

    t = 0
    x = 0
    y = h
    while y > 0:
        x, y = funcion(t)
        print(f"{x:.2f};{y:.2f};{t:.2f}")
        t = t + TIME_STEP