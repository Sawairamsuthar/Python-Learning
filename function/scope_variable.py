# def add(b):#  is local variable 
#     a=22
#     a+=10
#     print(a)
# add(99)
# print(a)
# scope of variable :-


# 
#! 1.local variable 
# bina tuple k output
# def add(b):
#     a=22
#     a+=10
#     return a,b
# res,res2=add(99)
# print(res)
# print(res2)

#! 2.global variable   
# the variable which is creted outside the functions is called as global variable 
# the scope of the global variable is inside the functions and out side functions i.e it can be accessible anywhere in our program .

# c=25
# def add (b=66):
#     a=22
#     global c 
#     c+= 5
#     print(c)
# add()

#! 3.  NON LOCAL  VARIABLE :
    # It is a variable which is neither global nor local variable .
#  It is uesed in the conecept of nested functions.

# def add(a):
#     c=33
#     def sub():
#         nonlocal c
#         c+=10
#         print(c)
#     sub()
# add(11)
# -----------------------------------------------------------------------------------------------------------------------------------------

# packing & unpacking 
# note :
# when we write '*' in functions declearations then it will pack the element 
# when we write '*' 









