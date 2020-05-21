class Person:
    def __init__(self,firstname="[no first name]",lastname="[no last name]"):
        self.firstname=firstname
        self.lastname=lastname
        self.eyecolor="[no eye color]"
        self.age=-1

myperson1=Person()
print(myperson1.firstname)
myperson2=Person("david","zazaf")
print(myperson2.firstname,myperson2.lastname)

