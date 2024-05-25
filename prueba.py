import requests

url = "http://127.0.0.1:8000//inference_cross_encoder"

# Datos a enviar en la petición
data = {
    "question": "This is an example test?",
    "total_chunks": ["Example chunk for dealing this case", "This is another case", "Yes, of course, this is an example test"]
}

# Enviar petición POST
response = requests.post(url, json=data)

# Comprobar respuesta
if response.status_code == 200:
    result = response.json()
    print(f"Resultado: {result} con los siguientes scores: ")
else:
    print(f"Error: {response.status_code}")
