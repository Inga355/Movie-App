from storage_json import StorageJson

storage = StorageJson('movies.json')
print(storage.list_movies())
storage.add_movie('Hello World', 2020, 2.0)
print(storage.list_movies())
storage.update_movie('Hello World', 10.0)
print(storage.list_movies())
storage.delete_movie('Hello World')
print(storage.list_movies())
print('Test solved')
