#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"

import os 
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_ATM = {
    'engine' : 'file_storage',
    'name' : 'accounts_gy',
    'path' : "%s/db" % BASE_DIR
}

LOG_LEVEL_ATM = logging.INFO
LOG_TYPES_ATM = {
    'transaction' : 'transactions.log',
    'access' : 'access.log'
}

TRANSACTION_TYPE_ATM = {
    'repay' : {'action' : 'plus','interest' : 0},
    'withdraw' : {'action' : 'minus','interest' : 0.05},
}