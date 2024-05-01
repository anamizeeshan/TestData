# def square(number):
#     return number **2
# result=square(4)
# print(result)
# def square(number):
#      return number **2
# #result=square(4)   result is not hold the answere
# print(square(4))
#----------------------------------------------------------------
#Q: functions with multtiple parameters
# def add(num1,num2):
#     return num1+num2
# print(add(5,5))
#------------------------------------------------------------------
#Q:polymorphism in funcations:write a function multiply that multiplies that multiplies two numbers,but also except two numbers and strings
# def multiply(p1,p2):
#     return p1*p2
# print(multiply(4,5))
# print(multiply("a",5))
# print(multiply(4,"a"))
#------------------------------------------------------------------
#Q:function returning multiple values:creat a function who creat both area and circumference of a circule of a given radius
# import math

# def circle_status(radius):
#    area = math.pi*radius**2
#    rounded_area=round(area,2)
#    circumference=2 * math.pi*radius 
#    rounded_circumference=round(circumference,2)
#    return rounded_area,rounded_circumference
# a,c=circle_status(3)
# print("Area",a,"circumference",c )
#------------------------------------------------------------------
#Q:defult parameter value:write a function that greet a user.if no name is pronided,it should greet to a defult name.
# def greet(name="user"):
#     return "hello "+name+"!"
# print(greet())#if we add name in a greet  it print a name and if name not added by defult user will print
#---------------------------------------------------------------
#Q:creat a lambda function to compute the cube of a number
# cube=lambda x: x ** 3   # its a one liner code we can write when we use one time code 

# print(cube(3))
#------------------------------------------------------------------
#Q:functions with *args:write a function that take variable number of arguments and return their sum
# def sum_all(*arg):# *args is used for multiple argument
#    return sum(arg)
# print(sum_all(1,2,))
# print(sum_all(1,2,3,4))
# print(sum_all(1,2,3,4,5,6,7,8,9,))
#-----------------*args in Python is not an iterator itself, but it allows you to pass a variable number 
# of arguments to a function. The *args syntax in a function definition collects any number of positional 
# arguments passed to the function into a tuple. You can then iterate over this tuple using a loop or any
# other method that works with tuples.----------------------------------
#def sum_all(*args):arg work as a iterater 
#    print(args)
#    for i in args:
#       print(i * 2)
#    return sum(args)
# print(sum_all(1,2,3))
#------------------------------------------------------------------------------
#Q:function with **kwargs:creat a function that accept any number of keyword arguments and print 
#them in the format key:value 
# def print_kwagrs(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key}:{value}")
# print_kwagrs(name="anam",power="lazer")
# print_kwagrs(name="anam")
# print_kwagrs(name="anam",Power="lazer",enemy="eggman")
#------------------------------------------------------------------------------------------------------        
#Q: generator function with yeild:write a generator function that yeild even numbers up to specified limit.
# def even_generator(limit):
#     for i in range(2,limit +1,2):
#         yield i

# for num in even_generator(10):
#     print(num)
#
#Q:recursive function:creat a recarsive function to calculate the factorial of a  number
# def factorial(n):
#     if n==0:
#         return 1
       
#     else:
#         return n * factorial(n-1)
# print(factorial(5)) 
#-------------------------------------------------------------------
#Q:WAF to print the length of a list
# names=["zeeshanAhmad","anam","ayesha"]
# cities=["lahore","ialamabad","karachi","Quetta","peshawar"]
# def length_list(list):
#     print(len(list))

# length_list(names)
# length_list(cities)
#--------------------------------------------------------------
#Q:WAF to print the element of a list in a single line 
# element=[1,2,3,4,5,6,7]
# cities=["lahore","ialamabad","karachi","Quetta","peshawar"]

# def print_line(list):
#     for item in list:
#         print(item,end="")
 
# print_line(element)
# result=0
# def factorial(n):
#     if n==0:
#       return 1
       
#     else:
#         return n * factorial(n-1)   
# print(factorial(9))    

# def factorial(n):
#    fact=1
#    for i in range(1,n+1):
#        fact*=i
#        print(fact)

# factorial(5)     
# def converter(USD_val):
#     Inr_val=USD_val*83
#     print(USD_val,"USD =",Inr_val," Inr")
# converter(7)    

# def check_number(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# check_number (8)
# --------------------------------------------------------------
#Q: find factorial using recursion
# def fact(n):
#     if(n==1) or (n==0):
#         return 1
#     return fact (n-1)*n
# print(fact(7))
# def fact(n):
#  if (n==0):
#    return 0
 
#  return fact(n-1) + n
 
# print(fact(5))
def print_list(list,indx=0):
    if indx==len(list):
        return
    print(list[indx])
    print_list(list,indx+1)

fruit=["mango","banana","apple","orange"]

print_list(fruit)    