#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
'''
main program handle module, handle all the user interaction
'''
import os,sys,json
from core import db_handler
from conf import settings



def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id
    :return:
    '''
    db_path_atm = db_handler.db_handler(settings.DATABASE_ATM)
    account_file_atm = "%s/%s.json" %(db_path_atm,account_id)
    print("account_file_atm is ",account_file_atm)
    if os.path.isfile(account_file_atm):
        with open(account_file_atm,"r") as f_atm:
            acc_data = json.load(f_atm)
            f_atm.close()
            return acc_data
    else:
        print("The account {} is not exsit !".format(account_id))
        return None

def dump_account(account_data):
    '''
    after updated transaction or account data, dump it back to file
    : return:
    '''
    db_path_atm =  db_handler.db_handler(settings.DATABASE_ATM)
    account_file_atm = '%s/%s.json' %(db_path_atm,account_data['id'])
    with open(account_file_atm,'w') as f_atm:
        json.dump(account_data,f_atm)
        f_atm.close()
    return True
