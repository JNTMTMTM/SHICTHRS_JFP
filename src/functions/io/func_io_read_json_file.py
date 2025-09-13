
import json
import copy

def read_json_file(path : str) ->dict:
    with open(path , "r" , encoding = "utf-8") as f:
        data = json.load(f)
        f.close()
        
    return data
