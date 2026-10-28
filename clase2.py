puerto_ingresado = "ochenta"  # Simula un input malicioso o incorrecto de un usuario

try:
    # 1. Tu turno: Intenta convertir el string a un entero usando int()
    # Pista: numero = int(variable_string)
    puerto_entero = int(puerto_ingresado)
    
    # 2. Tu turno: Usa un 'if' para verificar si el puerto es 80
    if puerto_entero == 80:
        print("El puerto es correcto (80).")
    else:
        print(f"El puerto {puerto_entero} es diferente al esperado.")
        
        # 3. Tu turno: Captura el error específico (ValueError) que ocurre al intentar 
        # # convertir la palabra "ochenta" en número.
except ValueError:
    print("[CRÍTICO] El valor ingresado no es un número válido. Revisa tus variables.")
