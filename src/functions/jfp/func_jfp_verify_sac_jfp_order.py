
from copy import deepcopy
import json
import json_fingerprint
from json_fingerprint import hash_functions

def verify_sac_jfp_order(data : dict) -> None:
    try:
        temp_dict : dict = deepcopy(data) 

        jsp = None

        # 加载json指纹
        jsp = temp_dict['sac_jfp']

        # 删除json指纹
        del temp_dict['sac_jfp']

        # 获取源数据指纹
        fingerprint = json_fingerprint.create(
                    input = json.dumps(temp_dict),
                    hash_function = hash_functions.SHA256,
                    version = 1
                )
        # print(jsp , fingerprint)
        # 匹配指纹
        if jsp == fingerprint.split('$')[2]:
            return True
        else:
            return False
    except:

        return False