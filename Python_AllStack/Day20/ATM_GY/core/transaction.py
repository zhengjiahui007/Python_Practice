#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"
'''
main program handle module, handle all the user interaction
'''
import os,sys,json
from conf import settings
from core import accounts



def make_transaction(log_obj,accountdata,action_type:str,amount,**other):
    '''
    deal all the user transactions
    :param accountdata : user account data
    :action_type : transaction type
    :amount : transaction amount
    :other : mainly for logging usage
    : return:
    '''
    amount_f = float(amount)
    if (action_type in settings.TRANSACTION_TYPE_ATM):
        interest_f = amount_f * settings.TRANSACTION_TYPE_ATM[action_type]['interest']
        old_balance = accountdata['balance']
        if ('plus' == settings.TRANSACTION_TYPE_ATM[action_type]['action']):
            new_balance = (old_balance + amount_f + interest_f)
        elif ('minus' == settings.TRANSACTION_TYPE_ATM[action_type]['action']):
            new_balance = (old_balance - amount_f - interest_f)
            if (0 > new_balance):
                print('''\033[31;1mYour credit [%s] is not enough for this transaction
                [%s] [%s]\033[0m'''%(accountdata['credit'],(amount_f + interest_f),old_balance))
                return None
        accountdata['balance'] = new_balance
        accounts.dump_account(accountdata) #save new data to file
        log_obj.info("account : %s   action : %s    amount : %s    interest : %s" %(accountdata['id'],action_type,amount,interest_f))
        return accountdata
    else:
        print("\033[31;1mTransaction type [%s] is not exist ! \033[0m" % (action_type))
        return None