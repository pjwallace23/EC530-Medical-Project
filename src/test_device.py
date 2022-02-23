import system as device
import logging

def test_check(self, Filename:str):
    if device.check_filetype(Filename):
        pass

def test_validate(self, Filename:str):
    if device.validate_json(Filename):
        pass

def test_send_measurements(self, Filename:str):
    if device.send_data(Filename):
        pass
