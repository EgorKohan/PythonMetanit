import os

'''
mkdir(): создает новую папку

rmdir(): удаляет папку

rename(): переименовывает файл

remove(): удаляет файл
'''

if os.path.exists("helloos"): os.rmdir("helloos")

os.mkdir("helloos")

print(os.path.exists("helloos"))

os.rename("helloos", "helloos2")

print(os.path.exists("helloos2"))

os.rmdir("helloos2")

