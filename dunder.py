#Magic methods

class test:
    def __init__(self):
        self.a=5

a = test()
# Printing out the object
print(a)

#Printing out the attributes of the object
print(dir(a))

class test2:
    def __init__(self):
        self.a=5
    
    def __str__(self):
        return str(self.a)

# We have overloaded the action of print on the object
a = test2()
print(a)