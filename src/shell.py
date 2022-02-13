import numpy as np
import sys
import logging
import classes
import system

def main():
    logging.basicConfig(filename='app.log', filemode='w', format='%(process)d - %(name)s - %(levelname)s - %(message)s')
    logging.info("main function started")
    while(1):
        print('Welcome to the medical application shell\n')
        func_to_do = input('Enter device or user: \n')
        if func_to_do == 'device':
            dev_id = input('device id: \n')
            dev_type = input('dev_type: \n')
            pat_id = input('pat_id: \n')
            data = input('device data: \n')
            system.add_device(dev_id, dev_type, pat_id, data)
        elif func_to_do == 'user':
            role = input('user role: \n')
            user_id = input('user id: \n')
            first = input('user first name: \n')
            last = input('user last name: \n')
            age = input('user age: \n')
            height = input('user height: \n')
            weight = input('user weight: \n')
            system.add_user(role, user_id, first, last, age, height, weight)
        else sys.stderr.write('invald input')
        exit_code = input('Enter q to quit application, anything else to continue: ')
        if exit_code == 'q':
            sys.exit()
        

if __name__ == '__main__':
    main()