'''
Handle all log info
'''

import logging
from conf import settings


def logger_atm(log_type:str):
    #creat logger
    logger_atm = logging.getLogger(log_type)
    logger_atm.setLevel(settings.LOG_LEVEL_ATM)

    # creat console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL_ATM)

    # creat file handler and set level to warning
    log_file_atm = "%s/log/%s" %(settings.BASE_DIR,settings.LOG_TYPES_ATM[log_type])
    fh = logging.FileHandler(log_file_atm)
    fh.setLevel(settings.LOG_LEVEL_ATM)

    # creat formatter to ch and fh
    formatter_atm = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter_atm)
    fh.setFormatter(formatter_atm)

    # add ch and fh to logger
    logger_atm.addHandler(ch)
    logger_atm.addHandler(fh)

    return logger_atm
