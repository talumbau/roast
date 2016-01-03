import json

def read_recipe(path):
    '''
    A simple function to read the JSON recipe format
    of Openroaster
    '''
    with open(path) as f:
        return json.load(f)


