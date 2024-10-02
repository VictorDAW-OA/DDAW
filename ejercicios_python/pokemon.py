import requests
from typing import List, Optional, Dict, Any
url = "https://pokeapi.co/api/v2/type"

def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    # Get the differents types of pokemons
    try:
        response = requests.get(url)
        response.raise_for_status() # Throws an exception if there is a problem with the request (4XX - 5XX)
    except Exception as e:
        print(f"Error con la excepcion: {e}")
        return None
    # Return data if the request was succesfull
    return response.json()

def get_water_type_url(data: Dict[str, any]) -> Optional[str]:
    # Get the url
    for pokemon in data['results']:
        if pokemon['name'] == "water":
            return pokemon['url']
    return None # If cant find the water url return none


def fetch_water_pokemons(url: str) -> List[str]:
    # Get the water type pokemons returns none if fails
    poke_dict = []
    response = requests.get(url) # Get a json list with all the water type pokemons
    data = response.json()
    if response.status_code == 200:
        for pokemon in data['pokemon']: 
            poke = pokemon['pokemon']['name'] # Adds all the pokemons to a dict
            poke_dict.append(poke)
        return poke_dict # Returns a dict with all the water type pokemons
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

