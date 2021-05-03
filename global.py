# Usage of global keyword in Python
a = 5

# function to perform addition
def add():
    a = a + 20
    print(a)
# This will produce error since a is a 'new' variable and it is being assigned to itself

def add2():
    global a
    a = 20
    print('Value of a from inside ', a)
    
  
# calling a function
print('Current value of a : ',a)
#add()
#The above command will error out
add2()
print('Current value of a :',a)
