def sumar(numeros: str) -> int:
    def sumar(numeros: str) -> int:
    # Si el string está vacío, retorna 0
        if not numeros:
            return 0
        
        # Divide por comas, convierte a entero y suma todo
        return sum(int(n) for n in numeros.split(","))
