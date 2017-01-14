class Student(object):
    def __init__(self,name,score):
        self._name = name
        self._score = score
    @property
    def AA(self): return self._score
    @AA.setter
    def AA(self,score):
        if not isinstance(score,int):
            raise ValueError("invalid score!!!")
        if score < 0 or score > 100:
            raise ValueError("score must be between [0,100]!!!")
        self._score = score
    @property
    def name(self): return self._name
s1 = Student("Lily", 120)
#s1.name = "Luly"
s1.AA = 130 # 这里相当于是 s1.AA(100)
# s1.name = "Luly"s1.AA = 100 # 这里相当于是 s1.AA(100)
