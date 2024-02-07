from imdb import IMDb

def get_actors_and_characters_from_title(title, ia):
    """Return a dictionary with actor names as keys and characters they played as values."""
    movie = ia.search_movie(title)[0]
    ia.update(movie, info=['full credits'])
    actors_and_characters = {cast['name']: cast.currentRole for cast in movie.get('cast', [])}
    return actors_and_characters

def main():
    ia = IMDb()

    title1 = input("Enter the name of the first movie/TV show: ").strip()
    title2 = input("Enter the name of the second movie/TV show: ").strip()

    # Fetch actors and their roles
    actors1 = get_actors_and_characters_from_title(title1, ia)
    actors2 = get_actors_and_characters_from_title(title2, ia)

    # Find common actors and sort them

    if common_actors := sorted(list(set(actors1.keys()).intersection(set(actors2.keys())))):
        print(f"Common actors between {title1} and {title2}:")
        for idx, actor in enumerate(common_actors, 1):  # Start numbering from 1
            roles1 = actors1[actor]
            roles2 = actors2[actor]
            print(f"{idx}. {actor} played as {roles1} in {title1} and as {roles2} in {title2}.")
    else:
        print(f"No common actors found between {title1} and {title2}.")

if __name__ == "__main__":
    main()
