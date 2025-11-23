# module is nothing but a python file which contains python code
from logging_utils import setting_up_logging
from vehicle import Car

from amazing_maths import amazing_div


def app_start():
    print('I am in app start function!')
    setting_up_logging()
    # amazing_maths.amazing_add(50, 100)
    amazing_div(100, 0)
    mahindra_thar = Car(name='Mahindra Thar', model='Thar Roxx')
    mahindra_thar.accelerate()


app_start()
