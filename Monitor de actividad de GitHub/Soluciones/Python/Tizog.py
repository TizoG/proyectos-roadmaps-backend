import requests

# ingresar el usuario de GitHub
username = input("Introduce el nombre del usuario de Github: ")

# consultar la activida reciente del usuario
URL = f"https://api.github.com/users/{username}/events"

response = requests.get(URL)

# mostrar la actividad reciente
data = response.json()

repositorios = {}


for event in data:
    if event["repo"]["name"] not in repositorios:
        repositorios[event["repo"]["name"]] = 1
    else:
        repositorios[event["repo"]["name"]] += 1


for repo, commits in repositorios.items():
    print(f"- Realizó {commits} commits en {repo}")


for event in data:
    # Inicializamos la variable lenguage con un valor predeterminado
    language = "No disponible"

    # Si el evento ees de tipo PullRequestsEvent, buscamos la informacion detallada
    if event["type"] == "PullRequestEvent":
        repo_details = event["payload"]["pull_request"]["head"]["repo"]
        # Usamos .get() para obtener el valor asociado a language
        language = repo_details.get("language", "Desconocido")

    # imprimimos el resultado
    print(f"Repositorio: {event["repo"]["name"]} - Lenguaje: {language}")
