def check_divide(dividend, divisor):
    """simple function to show how logs work
    """
    try:
        result = dividend/divisor
        return result
    except Exception as e:
        with open("logfile.txt", "a") as logfile:
            logfile.write(f"Error with dividing: {e}")

#check_divide(45, 55)
#check_divide(45, 0)



def check_divide(dividend, divisor):
    """simple function to show how logs work
    """
    try:
        result = dividend/divisor

        with open("logfile.txt", "a") as logfile:
            logfile.write(f"Dividing {dividend}/{divisor} was done.")
        return result
    except Exception as e:
        with open("logfile.txt", "a") as logfile:
            logfile.write(f"Error with dividing: {e}")
        raise Exception(f"Error with dividing: {dividend}/{divisor}.")

#check_divide(45, 55)
#check_divide(45, 0)


def write_to_log(log_message):
    with open("logfile.txt", "a") as logfile:
        logfile.write(log_message)


def check_divide(dividend, divisor):
    """simple function to show how logs work
    """
    try:
        result = dividend/divisor
        log_message = f"Dividing {dividend}/{divisor} was done."
        write_to_log(log_message)
        return result
    except Exception as e:
        log_message = f"Error with dividing: {dividend}/{divisor}."
        write_to_log(log_message)
        raise Exception(f"Error with dividing: {dividend}/{divisor}.")


#check_divide(45, 55)
#check_divide(45, 0)


from datetime import datetime
def write_to_log(log_message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    message = f"{dt_string}:{log_message}"
    with open("logfile.txt", "a") as logfile:
        logfile.write(message)


def check_divide(dividend, divisor):
    """simple function to show how logs work
    """
    try:
        result = dividend/divisor
        log_message = f"Dividing {dividend}/{divisor} was done."
        write_to_log(log_message)
        return result
    except Exception as e:
        log_message = f"Error with dividing: {dividend}/{divisor}."
        write_to_log(log_message)
        raise Exception(f"Error with dividing: {dividend}/{divisor}.")


#check_divide(45, 55)
#check_divide(45, 0)

