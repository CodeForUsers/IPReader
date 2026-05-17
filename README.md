# 🌐 IP Reader

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**IP Reader** es una herramienta elegante y sencilla escrita en Python que permite consultar información detallada sobre cualquier dirección IP (IPv4 o IPv6). Cuenta con una versión de terminal y una moderna interfaz web.

---

## ✨ Características

- 🔍 **Validación de IP:** Comprueba si la entrada es una dirección IPv4 o IPv6 válida.
- 🌐 **Información de Red:** Obtiene el CIDR, ASN, nombre del proveedor y la organización.
- 📍 **Geolocalización:** Muestra el país, ciudad, zona horaria y coordenadas (latitud y longitud).
- 🎨 **Interfaz Web:** Versión interactiva y visual con Streamlit.

---

## 🚀 Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

---

## 💻 Formas de Uso

Esta herramienta se puede utilizar de dos formas:

### 1. En la Terminal (Consola)
Ejecuta el script básico:
```bash
python3 ipreader.py
```
El programa te solicitará la IP y mostrará los resultados directamente en la consola.

### 2. Interfaz Web (Streamlit)
Ejecuta la aplicación web:
```bash
streamlit run ipreader_app.py
```
Esto abrirá una pestaña en tu navegador con una interfaz interactiva.

---

## 🌐 Formas de Despliegue (Deploy)

Si quieres que tu interfaz web esté accesible desde cualquier lugar, puedes desplegarla de forma sencilla:

### Opción A: Streamlit Community Cloud (Recomendado y Gratuito)
1. Sube tu código a un repositorio en **GitHub**.
2. Entra en [share.streamlit.io](https://share.streamlit.io/) y regístrate con tu cuenta de GitHub.
3. Haz clic en **"New app"**, selecciona tu repositorio, la rama y el archivo principal (`ipreader_app.py`).
4. ¡Haz clic en **"Deploy"**! Tu app estará lista en un par de minutos con una URL pública.

### Opción B: Docker (Para servidores propios)
Puedes crear un archivo `Dockerfile` con el siguiente contenido:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "ipreader_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
Luego construyes y corres el contenedor en tu servidor.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- **Biblioteca Requests:** Para las peticiones HTTP.
- **Biblioteca ipaddress:** Para la validación de IPs.
- **Streamlit:** Para la interfaz web.
- **API:** [ip.guide](https://ip.guide/)

---

## 👤 Autor

- **Nombre:** David Carreres Gómez
- **Fecha:** 18/05/2026
- **Versión:** 1.0
