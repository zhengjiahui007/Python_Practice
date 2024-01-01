#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
'''
main program handle module, handle all the user interaction
'''
import os,sys
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)
from core import logger,auth
from core import transaction,accounts

#transaction logger
trans_logger = logger.logger_atm('transaction')
#access_logger
access_logger = logger.logger_atm('access')

#temp account data,only save the data in memory
user_data = {
    'account_id' : None,
    'is_authenticated' : False,
    'account_data' : None
}

def account_info(acc_data):
    print(acc_data)
    return

def repay(acc_data):
    '''
    print current balance and let the user repay the bill
    : return:
    '''
    account_data_atm = accounts.load_current_balance(acc_data['account_id'])
    #or k,v in account_data_atm.items():
        #print(k,v)
    current_balance = '''-------- BALANCE INFO --------
        Credit    :    %s
        Balance   :    %s''' %(account_data_atm['credit'],account_data_atm['balance'])
    print(current_balance)
    back_flag = False
    while (not back_flag):
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if (0 < len(repay_amount) and (repay_amount.isdigit())):
            new_balance = transaction.make_transaction(trans_logger,account_data_atm,'repay',repay_amount)
            if (None != new_balance):
                print('''\033[42;1mNew Balance : %s\033[0m'''%(new_balance['balance']))
                return
        else:
            print('\033[31;1m[]%s is not a valid amount,only accept integer!\033[0m'%(repay_amount))
    return

def withdraw(acc_data):
    '''
    print current balance and let the user do the withdraw action
    : acc_data
    : return:
    '''
    account_data_atm = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''------- BALANCE INFO --------
        Credit    :    %s
        Balance   :    %s''' %(account_data_atm['credit'],account_data_atm['balance'])
    print(current_balance)
    back_flag = False
    while (not back_flag):
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if (0 < len(withdraw_amount) and (withdraw_amount.isdigit())):
            new_balance = transaction.make_transaction(trans_logger,account_data_atm,'withdraw',withdraw_amount)
            if (None != new_balance):
                print('''\033[42;1mNew Balance : %s\033[0m'''%(new_balance['balance']))
                return
        else:
            print('\033[31;1m[]%s is not a valid amount,only accept integer!\033[0m'%(withdraw_amount))
    return

def transfer(acc_data):
    pass
    return

def pay_check(acc_data):
    pass
    return

def logout(acc_data):
    exit()
    return

def interactive_atm(acc_data:dict):
    '''
    interact with user
    : return :
    '''
    menu_atm = u'''
    --------- OldBoy Bank ---------
    \033[32;1m
    1. Account Infomation
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
            print("\033[31;1mOption does not exist!\033[0m")


def decorator_gy_atm(func_gy):
    print("This is decorator_gy_atm!")
    def inner_gy_atm(*arg,**kwarg):
        print("This is {} , arg is {} , kwarg is {}!".format(func_gy.__name__,arg,kwarg))
        func_re = func_gy(*arg,**kwarg)
        return func_re
    return inner_gy_atm

@decorator_gy_atm
def run(param:int):
    '''
    This function will be called when program started
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive_atm(user_data)