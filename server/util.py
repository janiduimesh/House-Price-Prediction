import json
import pickle
__locations = None
__data_columns = None
__model = None

def get_location_names():
    pass

def load_saved_artifacts():
    print("Loading saved artifacts")
    global __data_columns
    global __locations
    
    with open("./artifacts.columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns['locations']
        
    with open("./artifacts/home_prices_model.pickle", "r") as f:
        __model = pickle.load(f)
    print("loading saved artifact..don")        
    
if __name__ == '__main__':
    print(get_location_names())    