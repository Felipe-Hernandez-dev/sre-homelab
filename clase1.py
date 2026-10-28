# 1. Declaración de variables
nombre_servicio = "Nginx"       # Esto es un String (str)
puerto_servicio = 80            # Esto es un Integer (int)
es_critico = True               # Esto es un Boolean (bool)

# 2. Tu turno: Declara una variable llamada 'ip_servidor' y asígnale la IP de tu LXC (como String)
ip_servidor = "192.168.78.185"

# 3. Tu turno: Imprime un log usando una f-string. 
# Debe decir exactamente: "El servicio Nginx está corriendo en la IP 192.168.78.185 por el puerto 80"
# (Usa las variables, NO escribas los datos a mano dentro del print)
print(f"El servicio {nombre_servicio} está corriendo en la IP {ip_servidor} por el puerto {puerto_servicio}")