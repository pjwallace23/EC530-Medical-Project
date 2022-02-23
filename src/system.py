from classes import User
from classes import Device
import json
import logging
import sys

active_users = {}
active_devices = {}
database = "database.json"

def add_user(role, user_id, first, last, age, height, weight):
    new_device = User(role, user_id, first, last, age, height, weight)
    active_users[user_id] = new_device
    return 1

def add_device(dev_id, dev_type, pat_id, data):
    new_device = Device(dev_id, dev_type, pat_id,data)
    active_devices[dev_id] = new_device
    return 1

def check_filetype(filename: str): # --> check filetype (1 if json, 0 if anything else)
    logging.info("Checking the filetype of inputted file: {filename}\n")

    fileN = filename.split(".")
    if (fileN[1] != 'json'):
        logging.info("invalid file format inputted\n")
        sys.stderr.write("non json file inputted\n")
        return 0

    else:
        logging.info("{filename} is a valid file")
        return 1

def validate_json(Json_file: str): # --> return 1 if valid json, 0 if not
    expected_keys = ['dev_id', 'dev_type', 'pat_id', 'data']
    is_json = check_filetype(Json_file)

    if is_json:
        logging.info("checking format of inputted json file: {Json_file}\n")
        open(Json_file, 'r') as fp
        data = json.load(fp)
        json_keys = data.keys()

        if (len(json_keys) != 4):
            logging.info("wrong amount of keys")
            return 0

        else:
            for item in expected_keys:
            if (item not in json_keys):
                logging.info("invalid json keys")
                return 0
            else:
                logging.info("valid json keys")
                return 1
    else:
        return 0

def send_data(Json_file: str): #  --> send a json file to the database
    
    val = validate_json(Json_file)
    if val == 0:
        return 0
    else:
        logging.info("Exporting to database")
        open(Json_file, 'r') as fp
        json_data = json.load(fp)

        open(database, 'w') as db
        json.dump(json_data, db, ensure_ascii=False, indent=4)
        logging.info("successfully exported")
        return 1

        


    