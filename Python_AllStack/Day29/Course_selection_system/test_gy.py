class BaseModel:
    def save(self):
        """
        使用pickle将用户对象保存到文件
        :return:
        """
        nid = str(self.nid)
        file_path = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_path, 'wb'))
    
    def ba_print(self):
        print(self.db_path,"3344 ")

class Admin(BaseModel):
    #db_path = "settings.ADMIN_DB"

    def __init__(self, username, password):
        """
        创建管理员对象
        :param username:
        :param password:
        :return:
        """
        # nid唯一ID，随机字符串
        #
        self.nid = "22342"  

obj = Admin(2,3)
print(type(obj))
obj.ba_print()