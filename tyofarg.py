# # There are two types of argument: Formal arguments & Actual arguments.
# #under Actual arguments : positional,keyword,default and variable length.
#
def person(name,age):
    print(name)
    print(age)

person('shaz',20) #example of positional arguments
#
# #################################################
#
# # i have defined this fn to somewhere else and we dont hae acess to this fn
# #and not sure about the sequence:
#
def person(name,age):
    print(name)
    print(age)

person(name='shaz',age=20) # using keyword for specifying parameters
#
# ##################################################################
#
def person(name,age=20): #parameters # using by default
    print(name)
    print(age)

person('shaz',20) #ARGUMENTS
# #when we dont pass age, by default it will give the default no
# # and if we pass age in  both default and parameters it is called override.
# #in override it will give the argument as output
#
# ##########################################################
#
def sum(a,*b):
    c = a+b
    print(c)

sum(2,3,4,5)  #2 will assign to a & rest of them will assign in b as a tuple
# # we cant simply add a int and tuple so will use *b
 # in the above given prog we wont get the ans as we cant add int and tuple simple so well use the below method
########################################################

def sum(a,*b):
    c = a

    for i in b:
        c=c+i
    print(c)

sum(1,2,3,4)

#############################################


def sum(*b):
    c = 0

    for i in b:
        c=c+i
    print(c)

sum(1,2,3,4)
