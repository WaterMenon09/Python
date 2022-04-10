class Phone:
    __brand = str()
    __volume = int()
    __mute = False

    def __init__(self, brand=None, volume=None, mute=None):
        if mute==None:
            self.__mute=False
        if brand != None:
            self.__brand = brand
        if volume!=None:
            self.__volume=volume

    def setMute(self, muted):
        self.__mute = muted

    def increaseVolume(self):
        if self.__volume<10:
            self.__volume+=1
        print(self.__volume)

    def decreaseVolume(self):
        if self.__volume>0:
            self.__volume-=1
        print(self.__volume)

    def __str__(self):
        if self.__mute:
            return str("The "+str(self.__brand)+" phone is currently muted at volume "+str(self.__volume))
        else:
            return str("The " + str(self.__brand) + " phone is currently unmuted at volume " + str(self.__volume))