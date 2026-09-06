storage=5000
files=20
size=256
total=files*size
files_in_storage=storage//size
free_space=storage%size
print('файлов в хранилище:', files_in_storage, 'свободное место:', free_space)