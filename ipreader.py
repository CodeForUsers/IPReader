"""
IP Reader es una herramienta que permite leer y consultar información sobre una IP, 
utilizando servicios externos de internet para obtener datos sobre la IP consultada.

Autor: David Carreres Gómez
Fecha: 18/05/2026
Version: 1.0

"""
import requests
import ipaddress

#Metodos
def validarIp(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
        

# Inicio del programa
# Solicitamos al usuario la dirección IP
dir_ip = input("Introduce la dirección IP: ")

#Validamos la dirección IP
if  not validarIp(dir_ip):
    print("La dirección IP no valida, asegurate que es una IP v4 o v6 valida.")
    exit()

# Consultamos a la API externa 
url = f"https://ip.guide/{dir_ip}"

respuesta = requests.get(url)

datos = respuesta.json()

# Imprimos los datos
print(f"\n INFO OBTENIDA DE LA IP: {datos.get('ip', dir_ip)}\n")

network = datos.get('network', {})
as_info = network.get('autonomous_system', {})
location = datos.get('location', {})

print(f"--- Red ---")
print(f"CIDR: {network.get('cidr', 'No disponible')}")
print(f"ASN: {as_info.get('asn', 'No disponible')}")
print(f"Proveedor: {as_info.get('name', 'No disponible')}")
print(f"Organización: {as_info.get('organization', 'No disponible')}")

print(f"\n--- Ubicación ---")
print(f"Pais: {location.get('country', 'No disponible')}")
print(f"Ciudad: {location.get('city', 'No disponible')}")
print(f"Zona Horaria: {location.get('timezone', 'No disponible')}")
print(f"Latitud: {location.get('latitude', 'No disponible')}")
print(f"Longitud: {location.get('longitude', 'No disponible')}")

