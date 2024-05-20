# This file contents secret keys and private information.
# Reading this would be a crime.
import os
from sqlalchemy import create_engine, text


#OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=os.environ['OMDB_APIKEY']

engine = create_engine(
    os.environ['AVIEN_DB_CONNECTION'],
    connect_args={"ssl": {"ca": ".certificates/ca.pem"}})

#engine = create_engine("postgresql://mvlist_user:mwluHr6FC2Jux9IxRuQGa8eUhSFUMHct@dpg-cp54ot8cmk4c73esodp0-a.oregon-postgres.render.com/mvlist",
#    isolation_level="REPEATABLE READ")


def loadMovies():
  with engine.connect() as conn:
    q = 'SELECT * FROM movies'
    result = conn.execute(text(q))

    rd = []
    for row in result.all():
      if len(rd) > 1000:  #limit shown results to this number
        return rd
      rd.append(row._asdict())

    return rd


def showMovie(id):
  with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM movies WHERE id = :id'),
                          {"id": id})
    rows = result.all()

    if len(rows) > 0:
      return rows[0]._asdict()
    return None
