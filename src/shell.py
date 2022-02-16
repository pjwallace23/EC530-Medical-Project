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
        file_to_input = input('Enter the device file to input: \n')
        if isinstance(file_to_input, str):
            system.send_data(file_to_input)
            logging.info("{file_to_input} sent to the database\n")
        else:
            logging.info("invalid input\n")
            sys.stderr.write('invald input\n')
        
        exit_code = input('Enter q to quit application, anything else to continue: ')
        if exit_code == 'q':
            sys.exit()
        

if __name__ == '__main__':
    main()