import json

def read_config():
    with open("config.json", "r") as f:
        return json.load(f)

def write_config(data):
    with open("config.json", "w+") as f:
        json.dump(data, f, indent=4)

def dict_unifier(*dicts_list :dict) -> dict:
    merged_dict = {}
    for dict_ in dicts_list:
        merged_dict.update(dict_)
    return merged_dict

