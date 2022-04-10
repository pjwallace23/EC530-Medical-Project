from classes import User
from classes import Device
import json
import logging
import sys
import sqlite3

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
    expected_keys = ['dev_id', 'dev_type', 'pat_id', 'b_pressure', 'pulse', 'weight', 'oximeter', 'temperature']
    is_json = check_filetype(Json_file)

    if is_json:
        logging.info("checking format of inputted json file: {Json_file}\n")
        open(Json_file, 'r') as fp
        data = json.load(fp)
        json_keys = data.keys()

        if (len(json_keys) != 8):
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

    conn = sqlite3.connect("medical_app.db")
    c = conn.cursor()

    val = validate_json(Json_file)
    if val == 0:
        return 0
    else:
        logging.info("Exporting to database")
        open(Json_file, 'r') as fp
        json_data = json.load(fp)

        d_id = json_data['dev_id']
        d_type = json_data['dev_type']
        p_id = json_data['pat_id']
        bp = json_data['b_pressure']
        pulse = json_data['pulse']
        weight = json_data['weight']
        o = json_data['oximeter']
        temp = json_data['temperature']

        c.execute("INSERT INTO device_data (dev_id, dev_type, pat_id, weight, temp, b_pressure, oximeter, pulse) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (d_id, d_type, p_id, weight, temp, bp, o, pulse))
        
        conn.commit()
        c.close()
        conn.close()

       
        return 1

        


    