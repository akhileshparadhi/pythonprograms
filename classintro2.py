class Classroom:
    def __init__(self,name,rank,roll_no):
        self.name = name
        self.rank= rank
        self.roll_no= roll_no

    def __repr__(self):
        return f"Name is {self.name} ,having {self.rank},whose roll no is {self.roll_no}"


student=Classroom("Akhilesh", 25 , 64)

print(student)