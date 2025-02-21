from storage_json import StorageJson
from movie_app import MovieApp
from storage_csv import StorageCsv

#storage = StorageJson('movies.json')
"""print(storage.list_movies())
storage.add_movie('Hello World', 2020, 2.0)
print(storage.list_movies())
storage.update_movie('Hello World', 10.0)
print(storage.list_movies())
storage.delete_movie('Hello World')
print(storage.list_movies())
print('Test solved')"""
#movie_app = MovieApp(storage)
#movie_app.run()




storage = StorageCsv('movies.csv')
movie_app = MovieApp(storage)
movie_app.run()