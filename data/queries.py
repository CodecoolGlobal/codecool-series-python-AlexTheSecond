from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_most_rated_shows(limit=15):
    return data_manager.execute_select("""
    SELECT title, year, runtime, rating,string_agg(genres.name, ', ')As genres ,trailer, homepage
    FROM shows
    INNER JOIN show_genres ON shows.id = show_genres.show_id
    INNER JOIN genres ON show_genres.genre_id = genres.id
    GROUP BY shows.id
    ORDER BY rating DESC LIMIT %(limit)s
    """, {'limit':limit})
