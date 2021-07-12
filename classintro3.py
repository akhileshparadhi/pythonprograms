class Classroom:

    SEX = ("Male","Female")


    def __init__(self,name,gender,roll_no):
        self.name = name
        self.gender= gender
        self.roll_no= roll_no

    def __repr__(self):
        return f"Name is {self.name} ,who is a {self.gender},whose roll no is {self.roll_no}"

    @classmethod
    def Male(cls,name,roll_no):
        return Classroom(name,Classroom.SEX[0],roll_no)




student=Classroom.Male("Akhilesh", 64)

print(student)