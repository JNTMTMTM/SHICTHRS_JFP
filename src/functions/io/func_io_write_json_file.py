
import json
import json_fingerprint
from json_fingerprint import hash_functions
from copy import deepcopy

def write_json_file(data : dict , path : str) -> None:
    # 获取写入的指纹
    fingerprint = json_fingerprint.create(
                input = json.dumps(data),
                hash_function = hash_functions.SHA256,
                version = 1
            )
    tempdata = deepcopy(data)
    
    tempdata['sac_jfp'] = fingerprint.split('$')[2]

    with open(path , "w", encoding = "utf-8") as f:
        json.dump(tempdata , f , ensure_ascii = False)
        f.close()