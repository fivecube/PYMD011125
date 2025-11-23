# This is amazing math module, and it contains logging for every math thing
# that you do.

import logging


def amazing_add(a, b):
    logging.info(f"We are going to add {a} and {b}")
    result = a + b
    logging.info(f"The result of adding {a} and {b} is {result}")
    return result


def amazing_div(a, b):
    logging.info(f"We are going to divide {a} by {b}")
    result = None
    try:
        result = a / b
        logging.info(f"The result of dividing {a} and {b} is {result}")
    except ZeroDivisionError as exc:
        logging.error(f'You can not divide by {b}')
    return result
