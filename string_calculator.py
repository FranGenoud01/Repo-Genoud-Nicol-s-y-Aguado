def sumar(numeros: str) -> int:
    if numeros == "":
        return 0
    
    partes = numeros.split(",")
    if len(partes) == 2:
        return int(partes[0]) + int(partes[1])
        
    return int(numeros)
