from datetime  import datetime as dt
class Player():

    __LVL , __HEALTH = 1, 100

    def __init__(self):
        self.__lvl  = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()
    @property
    def lvl(self):
        return self.__lvl
    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += numeric


    def info(self):
        print(self.__born)
c = Player()
c.lvl  = 100
print(c.lvl)
