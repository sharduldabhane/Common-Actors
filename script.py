from imdb import IMDb

def get_actors_from_title(title, ia):
    """Return a set of actors from the given title."""
    movie = ia.search_movie(title)[0]
    ia.update(movie, info=['full credits'])
    actors = {cast['name'] for cast in movie.get('cast', [])}
    return actors

def main():
    ia = IMDb()

    # Get movie/tv show names from user
    title1 = input("Enter the name of the first movie/TV show: ").strip()
    title2 = input("Enter the name of the second movie/TV show: ").strip()

    # Fetch actors
    actors1 = get_actors_from_title(title1, ia)
    actors2 = get_actors_from_title(title2, ia)


    # Find common actors
    common_actors = actors1.intersection(actors2)

    if common_actors:
        print(f"Common actors between {title1} and {title2}:")
        for actor in common_actors:
            print(actor)
    else:
        print(f"No common actors found between {title1} and {title2}.")

if __name__ == "__main__":
    main()
