def sumar(numeros: str) -> int:
    if not numeros:
        return 0
    
    numeros_limpios = numeros.replace("\n", ",")
    return sum(int(n) for n in numeros_limpios.split(","))
