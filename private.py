# Private variables in python
#  There are no access specifiers in Python and hence no private variables
# However there are certain 

class Test:
    def __init__(self):
        self.public = 3
        self._protect = 4
        self.__private = 5

a = Test()

# The "public" part is obvious
print(f'The public variable is : {a.public}')

# "Protected" is still accessible but the '_' serves as a caution
print(f'The protected variable is : {a._protect}')

# "Private" is inaccessible as Python mangles the anmes of any variables that begin '__'.
#  The next line should error out.
# print(f'The private variable is : {a._private}')

# Python manges the name of '__'-variables by appending a '_class-name_' in front of their names
print(f'The protected variable is : {a._Test__private}')





