
# if no bass class for all of the father class, search from left class(son to father) to right class one by one
# if a bass class for all of the father class,search from left class(do not search the bass class),then search the right class
""" 
class bass_gy():
    def gy_a0(self):
        print("bass_gy gy_a0!")
        return None

    def gy_a(self):
        print("bass_gy gy_a1!")
        return None


class f_gy(bass_gy):
    def gy_a01(self):
        print("f_gy gy_a0!")
        return None

    def gy_a(self):
        print("f_gy gy_a1!")
        return None


class f0_gy(f_gy):
    def gy_a01(self):
        print("f0_gy gy_a0!")
        return None

    def gy_a1(self):
        print("f0_gy gy_a1!")
        return None

class f1_gy(bass_gy):
    def gy_a01(self):
        print("f1_gy gy_a1!")
        return None

    def gy_a1(self):
        print("f1_gy gy_a1!")
        return None

class s0_gy(f0_gy,f1_gy):
    pass

class s1_gy(f1_gy,f0_gy):
    pass

obj_gy = s0_gy()
obj_gy.gy_a0()
 """
# obj1_gy = s1_gy()
# obj1_gy.gy_a0()

class bass_gy():
    def gy_a0(self):
        print("bass_gy gy_a0!")
        return None

class f_gy(bass_gy):
    def gy_a0(self):
        print("f_gy gy_a0!")
        self.gy_a1() #self is the real object (obj1_gy) of class
        return None

    def gy_a1(self):
        print("f_gy gy_a1!")
        return None   

class f0_gy():
    def gy_a1(self):
        print("f0_gy gy_a1!")
        return None


class s0_gy(f0_gy,f_gy):
    pass


obj1_gy = s0_gy()
obj1_gy.gy_a0()