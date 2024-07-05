import requests
import pandas as pd
import os

# URL dasar untuk PokeAPI
base_url = "https://pokeapi.co/api/v2/ability/"

# Fungsi untuk mengambil data dari PokeAPI
def fetch_ability_data(ability_id):
    url = base_url + str(ability_id)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        effect_entries = data['effect_entries']
        abilities = []
        for entry in effect_entries:
            ability = {
                "id": ability_id,
                "pokemon_ability_id": data['id'],
                "effect": entry.get('effect', ''),
                "language": entry.get('language', {}).get('name', ''),
                "short_effect": entry.get('short_effect', '')
            }
            abilities.append(ability)
        return abilities
    else:
        return [{
            "id": ability_id,
            "pokemon_ability_id": ability_id,
            "effect": "",
            "language": "",
            "short_effect": ""
        }]

# Menyimpan data ke CSV per 100 data
def save_to_csv(data, start, end):
    df = pd.DataFrame(data)
    filename = f'result_{start}_{end}.csv'
    df.to_csv(filename, index=False)
    return filename

# Main function
def main():
    all_data = []
    
    for start in range(1, 1000, 100):
        end = min(start + 99, 999)
        batch_data = []
        for i in range(start, end + 1):
            batch_data.extend(fetch_ability_data(i))
        csv_filename = save_to_csv(batch_data, start, end)
        all_data.extend(batch_data)
        print(f'{csv_filename} has been created.')

    # Optionally, return the combined data
    return all_data

if __name__ == '__main__':
    main()