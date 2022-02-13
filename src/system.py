from classes import User
from classes import Device

active_users = {}
active_devices = {}

def add_user(role, user_id, first, last, age, height, weight):
    new_device = User(role, user_id, first, last, age, height, weight)
    active_users[user_id] = new_device

def add_device(dev_id, dev_type, pat_id, data):
    new_device = Device(dev_id, dev_type, pat_id,data)
    active_devices[dev_id] = new_device

    