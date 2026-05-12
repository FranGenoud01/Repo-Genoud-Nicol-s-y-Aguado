def sumar(numeros: str) -> int:
    if not numeros:
        return 0
    
    delimitador = "," 
    
    if numeros.startswith("//"):
        partes = numeros.split("\n", 1) 
        encabezado = partes[0]  
        delimitador = encabezado[2:]  
        numeros = partes[1]  
    
    numeros_limpios = numeros.replace("\n", ",").replace(delimitador, ",")
    
    return sum(int(n) for n in numeros_limpios.split(","))