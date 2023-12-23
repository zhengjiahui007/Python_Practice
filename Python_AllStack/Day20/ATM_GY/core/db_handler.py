#!_*_coding:utf-8_*_
#!__author__:"Garry Zheng"


def file_db_handle(conn_params:dict):
    '''
    parse the db file path
    :param conn_parms : the db connection params set in settings
    : return : a
    '''
    db_path_atm = '%s/%s' %(conn_params['path'],conn_params['name'])
    return db_path_atm

def db_handler(conn_parms:dict):
    '''
    connect to db
    :param conn_parms : the db connection params set in settings
    : return : a
    DATABASE_ATM = {
    'engine' : 'file_storage',
    'name' : 'accounts',
    'path' : "%s/db" % BASE_DIR
    }
    '''

    if ('file_storage' == conn_parms['engine']):
        return file_db_handle(conn_parms)