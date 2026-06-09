def conectar_base_de_datos():
    # SonarCloud va a detectar esto como un Blocker de seguridad
    contraseña_db = "12345_admin_super_secreta"
    usuario = "root"
    print(f"Conectando con {usuario} y la clave {contraseña_db}")

def agregar_producto(producto, carrito=[]):
    # Bug: El carrito muta y guarda cosas de ejecuciones anteriores
    carrito.append(producto)
    return carrito

def calcular_cosas_raras():
    variable_inutil = 42  # Code Smell: Variable asignada pero nunca usada
    
    if True:
        if True:
            if True:
                # Code Smell: Demasiada anidación
                print("Esto es muy difícil de leer")
                return True

def hacer_calculo_complejo_uno(a, b):
    resultado = a + b
    resultado = resultado * 2
    resultado = resultado - 1
    return resultado

# Duplicación exacta de la lógica anterior
def hacer_calculo_complejo_dos(a, b):
    resultado = a + b
    resultado = resultado * 2
    resultado = resultado - 1
    return resultado