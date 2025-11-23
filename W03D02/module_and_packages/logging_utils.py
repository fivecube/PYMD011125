import logging
from datetime import datetime, timedelta

current_time = datetime.now()
print('i am happy to be here!')
print(current_time)


def setting_up_logging():
    logging.basicConfig(
        filename='log_files/module_and_packages.log',
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
