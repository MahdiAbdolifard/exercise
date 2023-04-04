"""
    Person
        creat fullname from person 
        creat gmail from person
"""

class Person:
    def __init__(self, fname:str, lname:str):
        self.fname = fname
        self.lname = lname

    def fullname(self) ->str:
        return f"{self.fname} {self.lname}"
    
    def gmail(self) ->str:
        return f"{self.fullname()}@gmail.com".replace(" ", "")
        

p1= Person('mahdi', 'abdolifard')

print(p1.fullname())
print(p1.gmail())