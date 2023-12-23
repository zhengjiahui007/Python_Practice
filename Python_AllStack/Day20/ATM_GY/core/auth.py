#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"

import os,time,sys,json
from core import db_handler
from conf import settings

def acc_auth(account,pwd):
    '''
    account auth func
    :param account : credit account number,pwd : card pwd
    :return : if passed, return the account obj, other 
    '''
    db_path_atm = db_handler.db_handler(settings.DATABASE_ATM)
    account_file_atm = "%s/%s.json" %(db_path_atm,account)
    print("account_file_atm is ",account_file_atm)
    if os.path.isfile(account_file_atm):
        with open(account_file_atm,"r") as f_atm:
            account_data = f_atm.read()
            f_atm.close()
            account_data_dic = json.loads(account_data)
            if (pwd == account_data_dic['password']):
                exp_time_stamp = time.mktime(time.strptime(account_data_dic['expire_date'],"%Y-%m-%d"))
                if (exp_time_stamp < time.time()):
                    print("The %s is expired, please contact the bank !" %(account))
                    return None
                else:
                    return account_data_dic
            else:
                print("\033[31;lmAccount [%s] does not exist !\033[0m" %account)
                return None
    else:
        return None


def acc_login(user_data:dict,log_obj):
    '''
    account login func,
    :user_data : user info data,only save in memory
    :return:
    '''
    retry_count = 0
    while ((user_data['is_authenticated'] is not True) and (3 > retry_count)):
        account_atm = input("\033[32;lmaccount:\033[0m").strip()
        password_atm = input("\033[32;lmpassword:\033[0m").strip()
        auth_atm = acc_auth(account_atm,password_atm)
        if (None != auth_atm):
            user_data['is_authenticated'] = True
            user_data['account_id'] = account_atm
            return auth_atm
        retry_count += 1
    else:
        log_obj.error("account [%s] too many loging attempts" %account_atm)
        exit()
