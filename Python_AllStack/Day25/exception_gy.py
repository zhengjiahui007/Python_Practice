

class GY_Except(Exception):
    pass
    # def __init__(self, ex_gz:str):
    #     self.message = ex_gz
    #     return None
    
   # def __str__(self):
     # return self.message


def test_exception_gz(a_gz:int,b_gz:str):
    try:
        print(a_gz,b_gz)
        a = int(b_gz)
        assert (type(a) is not int),"An assert occurred !"

        print(type(a) is not int,type(a),type(a) is int,type(b_gz) is str)
        param_flag_bool = (type(a) is not int) if (type(a) is not int) else (type(b_gz) is str)
        if param_flag_bool:
            raise Exception("a is not int, please input a int")
        if param_flag_bool:
            raise GY_Except("An GY_Except occurred !")
    except IndexError as e:
        print('An IndexError occurred e is ',e)
    except ValueError:
        print('An ValueError occurred')
    except GY_Except as e:
        print('An GY_Except occurred e is ',e)
    except Exception as e:
        print('An exception occurred e is ',e)
    else:
        print("No exception occured !")
    finally:
        print("The last come here  !")
    

test_exception_gz(4,"9")
#test_exception_gz(4,"DD")