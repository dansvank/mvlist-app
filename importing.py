from sqlalchemy import create_engine, text
import os, csv

filepath = "movies.csv"

engine = create_engine(
    os.environ['DB_CONNECTION_STRING'],
    connect_args={"ssl": {
        "ca": "/etc/ssl/certs/ca-certificates.crt"
    }})

with open(filepath) as f, engine.connect() as conn:
  csvFile = csv.DictReader(f)

  for line in csvFile:
    print("Importing: ", line["title_main"])

    data = {
        "title_main":
        str(line["title_main"]),
        "title_original":
        str(line["title_original"]),
        "release_year":
        int(line["release_year"]),
        "runtime":
        str(line["runtime"]),
        "country":
        str(line["country"]),
        "language_":
        str(line["language_"]),
        "director":
        str(line["director"]),
        "production":
        str(line["production"]),
        "genre":
        str(line["genre"]),
        "top_cast":
        str(line["top_cast"]),
        "plot":
        str(line["plot"]),
        "rating_imdb":
        str(line["rating_imdb"]) if len(line["rating_imdb"]) > 0 else None,
        "rating_metacritic":
        str(line["rating_metacritic"])
        if len(line["rating_metacritic"]) > 0 else None,
        "rating_rottentomatoes":
        str(line["rating_rottentomatoes"])
        if len(line["rating_rottentomatoes"]) > 0 else None,
        "imdb_id":
        str(line["imdb_id"]),
        "website":
        str(line["website"]),
        "trailer":
        str(line["trailer"]),
        "poster_small":
        str(line["poster_small"]),
        "poster_large":
        str(line["poster_large"]),
        "connections":
        str(line["connections"]),
        "quality":
        str(line["quality"]),
        "subtitles":
        str(line["subtitles"])
    }

    q = "INSERT INTO movies (title_main, title_original, release_year, runtime, country, language_, director, production, genre, top_cast, plot, rating_imdb, rating_metacritic, rating_rottentomatoes, imdb_id, website, trailer, poster_small, poster_large, connections, quality, subtitles) VALUES (:title_main, :title_original, :release_year, :runtime, :country, :language_, :director, :production, :genre, :top_cast, :plot, :rating_imdb, :rating_metacritic, :rating_rottentomatoes, :imdb_id, :website, :trailer, :poster_small, :poster_large, :connections, :quality, :subtitles)"
    conn.execute(text(q), data)
'''
#line is already a dict with the keys we need,
#but I'm making sure the datatype is correct
    
'''
