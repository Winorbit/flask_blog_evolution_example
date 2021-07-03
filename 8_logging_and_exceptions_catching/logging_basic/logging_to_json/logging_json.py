import logging  
import logging.config  
import json

with open("logging_config.json", 'r') as logger_config:  
    config_dict = json.load(logger_config)  
  
logging.config.dictConfig(config_dict)  
  
# Запись о том, что logger настроен  
logger = logging.getLogger(__name__)  
logger.info('Настройка логгирования окончена!')



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

