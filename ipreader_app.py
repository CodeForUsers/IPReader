import streamlit as st
import requests
import ipaddress

# Método para validar la IP
def validar_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Configuración de la página
st.set_page_config(
    page_title="IP Reader - Buscador de IP",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo personalizado simple
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌐 IP Reader")
st.write("Consulta información detallada sobre cualquier dirección IP (IPv4 o IPv6).")

# Input del usuario
dir_ip = st.text_input("Introduce la dirección IP:", placeholder="Ej: 2a0c:5a87:101:d800:f773:914c:541c:becc")

if st.button("Consultar Información"):
    if not dir_ip:
        st.warning("⚠️ Por favor, introduce una dirección IP.")
    elif not validar_ip(dir_ip):
        st.error("❌ La dirección IP no es válida. Asegúrate que es una IPv4 o IPv6 válida.")
    else:
        with st.spinner("Buscando información..."):
            try:
                url = f"https://ip.guide/{dir_ip}"
                respuesta = requests.get(url)
                
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    
                    st.success(f"✅ Información obtenida para la IP: **{datos.get('ip', dir_ip)}**")
                    
                    # Crear dos columnas para organizar la información
                    col1, col2 = st.columns(2)
                    
                    network = datos.get('network', {})
                    as_info = network.get('autonomous_system', {})
                    location = datos.get('location', {})
                    
                    with col1:
                        st.markdown("### 📡 Datos de Red")
                        st.write(f"**CIDR:** `{network.get('cidr', 'No disponible')}`")
                        st.write(f"**ASN:** `{as_info.get('asn', 'No disponible')}`")
                        st.write(f"**Proveedor:** {as_info.get('name', 'No disponible')}")
                        st.write(f"**Organización:** {as_info.get('organization', 'No disponible')}")
                        
                    with col2:
                        st.markdown("### 📍 Ubicación")
                        st.write(f"**País:** {location.get('country', 'No disponible')}")
                        st.write(f"**Ciudad:** {location.get('city', 'No disponible')}")
                        st.write(f"**Zona Horaria:** {location.get('timezone', 'No disponible')}")
                        st.write(f"**Latitud:** `{location.get('latitude', 'No disponible')}`")
                        st.write(f"**Longitud:** `{location.get('longitude', 'No disponible')}`")
                        
                else:
                    st.error(f"❌ No se pudo obtener información. Código de estado: {respuesta.status_code}")
                    
            except Exception as e:
                st.error(f"❌ Ocurrió un error al conectar con la API: {e}")

# Pie de página
st.markdown("---")
st.markdown("Desarrollado por David Carreres Gómez | Versión 1.0")
