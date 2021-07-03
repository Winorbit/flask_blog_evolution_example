import logging
'''
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''

def check_divide(dividend, divisor):
    """simple function to show how logs work
    """
    try:
        result = dividend/divisor
        log_message = f"Dividing {dividend}/{divisor} was done."
        logging.info(log_message)
        return result
    except Exception as e:
        log_message = f"Error with dividing: {dividend}/{divisor}."
        logging.error(log_message)
        raise Exception(log_message)


#check_divide(45, 55)
#check_divide(45, 0)

logging.basicConfig(**logger_conf)

logging.basicConfig(filename='logfile.log', 
                    filemode='a', 
                    format='%(funcName)s  :: %(levelname)s :: %(message)s')

#logging.warning('This will get logged to a file')


def check_divide(dividend, divisor):
    """simple function to show how logs work
    """
    try:
        result = dividend/divisor
        log_message = f"Dividing {dividend}/{divisor} was done."
        logging.info(log_message)
        return result
    except Exception as e:
        log_message = f"Error with dividing: {dividend}/{divisor}."
        logging.error(log_message)
        raise Exception(log_message)

check_divide(45, 55)
check_divide(45, 0)

