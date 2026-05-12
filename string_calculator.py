def sumar(numeros: str) -> int:
<<<<<<< HEAD
    # Si el string está vacío, retorna 0
    if not numeros:
        return 0
    
    # Divide por comas, convierte a entero y suma todo
    return sum(int(n) for n in numeros.split(","))
=======
    if numeros == "":
        return 0
    
    partes = numeros.split(",")
    if len(partes) == 2:
        return int(partes[0]) + int(partes[1])
        
    return int(numeros)
>>>>>>> c3e77620ed6f1d77e6f122b9beb257257700c915
