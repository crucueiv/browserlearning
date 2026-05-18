import requests

def load_web_url(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url  # Agregar prefijo http si no está presente
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error al cargar la página: {e}"

def load_local_url(url):
    with open(url, 'r', encoding='utf-8') as file:
        return file.read()

def load_url(url):
    try:
        if url.startswith("file://"):
                url = url.replace("file://", "", 1)  # Eliminar el prefijo "file://"
                return load_local_url(url)
        else:
            return load_web_url(url)
    except Exception as e:
        return f"Error al cargar la URL: {e}" 