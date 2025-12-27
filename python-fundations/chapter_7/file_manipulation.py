import os

folder = '/Users/I772397/Coding/python-course/python-fundations'
entries = os.scandir(folder)

for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory:', entry.name)