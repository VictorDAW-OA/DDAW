import requests
from typing import List, Optional, Dict, Any
url = "https://pokeapi.co/api/v2/type"

def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    # Get the differents types of pokemons
    response = requests.get(url)
    if(response.status_code == 200):
       return response.json()
    else:
        print("Error con la peticion, error: "+response.status_code)
        return None

def get_water_type_url(data: Dict[str, any]) -> Optional[str]:
    # Get the url
    for pokemon in data['results']:
        if pokemon['name'] == "water":
            return pokemon['url']
    return None


def fetch_water_pokemons(url: str) -> List[str]:
    # Get the water type pokemons returns none if fails
    pokeDict = []
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        for pokemon in data['pokemon']:
            poke = pokemon['pokemon']['name']
            pokeDict.append(poke)
        return pokeDict
    else:
        print("Error a fetch tipo agua"+ data.status_code)
        return None

def display_pokemons(pokemons: List[str]) -> None:
    # Prints all the pokemons names
    for pokemon in pokemons:
        print(pokemon)

if __name__ == "__main__":
    
    data = fetch_data(url)
    # Get the url with water type
    water_type_url = get_water_type_url(data)

    # Check if we have the url
    if water_type_url:
        water_pokemons = fetch_water_pokemons(water_type_url)
        display_pokemons(water_pokemons)
    else:
        print("No se encontro el tipo agua")

