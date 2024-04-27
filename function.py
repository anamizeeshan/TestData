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