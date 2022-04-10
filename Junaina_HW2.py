class Student:
    __name = str()
    __Exam1 = None
    __Exam2 = None

    def __init__(self, name, a=None, b=None):
        self.__name = name
        if a!=None:
            self.__Exam1=a
        if b!=None:
            self.__Exam2=b

    def __str__(self):
        return ("Student: "+ self.__name+"\n\tExam1: "+str(self.__Exam1)+"\n\tExam2: "+str(self.__Exam2))

    def getName(self):
        print(self.__name)
    def setExam1Grade(self,grade):
        self.__Exam1=grade
    def setExam2Grade(self,grade):
        self.__Exam2=grade
    def getExam1Grade(self):
        if self.__Exam1==None:
            return None
        else:
            print(self.__Exam1)
    def getExam2Grade(self):
        if self.__Exam2==None:
            return None
        else:
            print(self.__Exam2)
    def getAverage(self):
        if self.__Exam1==None or self.__Exam2==None:
            print("Some exam grades not available.")
        else:
            print(float(self.__Exam1+self.__Exam2)/2)