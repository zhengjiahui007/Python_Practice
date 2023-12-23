#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
'''
main program handle module, handle all the user interaction
'''
import os,sys
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)
from core import logger,auth

#transaction logger
trans_logger = logger.logger_atm('transaction')
#access_logger
access_logger = logger.logger_atm('access')

#temp account data,only save the data in memory
user_data = {
    'accound_id' : None,
    'is_authenticated' : False,
    'account_data' : None
}

def account_info(acc_data):
    pass
    return

def repay(acc_data):
    pass
    return

def withdraw(acc_data):
    pass
    return

def transfer(acc_data):
    pass
    return

def pay_check(acc_data):
    pass
    return

def logout(acc_data):
    pass
    return

def interactive_atm(acc_data:dict):
    '''
    interact with user
    : return :
    '''
    menu_atm = u'''
    --------- OldBoy Bank ---------
    \033[32;lm
    1. Account INfomation
    2. Repay
    3. Withdraw
    4. Transfer
    5. Bill detail
    6. Logout
    \033[0m
    '''
    menu_dic_atm = {
        '1' : account_info,
        '2' : repay,
        '3' : withdraw,
        '4' : transfer,
        '5' : pay_check,
        '6' : logout,
    }
    exit_flag_atm = False
    while (not exit_flag_atm):
        print(menu_atm)
        user_option = input(">> : ").strip()
        if user_option in menu_dic_atm.keys():
            menu_dic_atm[user_option](acc_data)
        else:
            print("\033[31;lmOption does not exist!\033[0m")

def run(param:int):
    '''
    This function will be called when program started
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive_atm(user_data)