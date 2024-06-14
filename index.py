class student():
    def __init__(self , name ,std ,age):
        self.name = name
        self.std = std
        self.age = age
    def sname(self):
        print(f"{self.name}")
        print(self.std)



a = student("ooo",15,20)
a.sname()
