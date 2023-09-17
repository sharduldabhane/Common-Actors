# Movie/Tv Show Common Actor Finder

This script helps to find common actors between two movies or TV shows and provides details on the roles they played in each.

## Requirements

- Python 3.x
- IMDbPY package. You can install it using `pip`:

pip install IMDbPY


## Usage

1. Run the script:

python script_name.py


Replace `script_name.py` with the name you saved the script as.

2. You will be prompted to enter the names of two movies or TV shows.
3. The script will then display any common actors and the roles they played in each title.

## Functionality

The script primarily contains two main functions:

- `get_actors_and_characters_from_title(title, ia)`: 
Fetches a dictionary with actor names as keys and the roles they played in the given title as values.

- `main()`: 
Executes the main logic of the script - takes user input for movie/TV show titles, fetches the actors and roles using the IMDbPY API, determines common actors and displays the result.

## Note

The accuracy and availability of the data depend on the IMDbPY package and IMDb's data.
