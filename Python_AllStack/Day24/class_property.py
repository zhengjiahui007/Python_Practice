class Harman_gz():
    def __init__(self) -> None:
        return None

    @property
    def har_propprint(self):
        print("This is property !")
        return 4


obj_gz = Harman_gz()
print(obj_gz.har_propprint)