import requests
import sys

def check_service(ip: str, puerto: int) -> bool:
    """Verifica si un servicio HTTP está respondiendo con código 200."""
    url = f"http://{ip}:{puerto}"
    print(f"[INFO] Inspeccionando servicio en {url}...")
    
    try:
        # Hacemos la petición con un timeout corto para no quedarnos colgados (buenas prácticas)
        respuesta = requests.get(url, timeout=3)
        
        # Evaluamos el código HTTP
        if respuesta.status_code == 200:
            print(f"[SUCCESS] El servicio está OPERATIVO (HTTP 200).")
            return True
        else:
            print(f"[WARNING] El servicio respondió con código anómalo: {respuesta.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        # Capturamos cualquier explosión de red (timeout, connection refused, dns failure)
        print(f"[CRÍTICO] Fallo catastrófico de red. Detalle: {e}")
        return False

# Escudo de modularidad
if __name__ == "__main__":
    # Materia prima (apuntando a tu Nginx en LXC)
    nodo_ip = "192.168.78.185" 
    nodo_puerto = 8080
    
    # Invocamos la función
    esta_saludable = check_service(nodo_ip, nodo_puerto)
    
    # Reportamos al Sistema Operativo
    if esta_saludable:
        print("[EXIT 0] Aprobado para producción.")
        sys.exit(0)
    else:
        print("[EXIT 1] Fuego en producción. Abortando pipeline.")
        sys.exit(1)
