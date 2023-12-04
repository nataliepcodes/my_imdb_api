import csv

def get_genre(genre):
    file = "imdb-movie-data.csv"
    result = list()
    with open (file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if genre in row["Genre"]:
                # append the row - all data about the movie for that genre, not only the Title (row["Title"])
                result.append(row)
    return result
