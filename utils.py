import ipaddress
import requests

def validar_ip(ip):
    """Valida si una cadena es una dirección IPv4 o IPv6 válida."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def consultar_ip(ip, timeout=10):
    """Consulta la API de ip.guide con manejo de errores y timeout."""
    url = f"https://ip.guide/{ip}"
    try:
        respuesta = requests.get(url, timeout=timeout)
        if respuesta.status_code == 200:
            return respuesta.json(), None
        else:
            return None, f"Error: La API respondió con código {respuesta.status_code}"
    except requests.exceptions.Timeout:
        return None, "Error: La solicitud tardó demasiado tiempo (Timeout)."
    except requests.exceptions.RequestException as e:
        return None, f"Error de conexión: {e}"
