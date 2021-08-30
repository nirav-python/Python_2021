# # # Declaring three unique variables:
A,a,z = "Nirav", 1.3, 9
print(A)
print(a)

# #Swap complex variable with integer one:
a= 3 + 6j
b= 9

a,b = b,a
print ("a=", a)

# Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.
usr = input("Enter your UID: ")
print (usr)

# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

x = input("Enter anything between 1-10: ")
y= input("Enter anything between 1-10:")

z= float(x)+float(y)
print(z)

#  Write a program to check the data type of the entered values.
x = "Nirav"
print ("The type of the input is :", type(x))

#Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE:

ExampleForUpperCamelCase
exampleForLowerCamelCase
example_for_snakeCase
EXAMPLEFORUPPERCASE

# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?

Yes, every time new value is assigned to 'a', it will overwrite the previously assigned value.

#OPERATORS AND DECISION MAKING STATEMENT- Part2

a=int(input("Please enter your value:"))
if(a%3==0):
    print("ConsultAdd")
if(a%5==0):
    print("Python Training")
if(a%3==0) and (a%5==0):
    print("ConsultAdd-Python training")

#

print("Please select your selector choice:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Average")

ch=int(input("Enter Choice from(1-5): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Result = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Result = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Result = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Result = ",c)
elif ch==5:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=(a+b) / 2
    print("Result = ",c)
else:
    print("Incorrect Choice")


#Flowchart

a = 10
b = 20
c = 30
avg = (a+b+c)/3
print('avg= ', avg)
if avg > a and avg > b and avg > c:
    print('avg is higher than a, b, c')
elif avg > a and avg > b:
    print('avg is higher than a, b')
elif avg > a and avg > c:
    print('avg is higher than a, c')
elif avg > b and avg > c:
    print('avg is higher than b, c')
elif avg > a:
    print('avg is just higher than a')
elif avg > b:
    print('avg is just higher than b')
elif avg > c:
    print('avg is just higher than b')


#Write a program in Python to break and continue if the following cases occurs:
while True:
    i = input('Please enter a number:')
    i = int(i)
    if i >= 0:
        print("Good Going!")
        break
    print("Its over")


# #Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.
list = [i for i in range(2000, 3201) if i % 7 == 0 if i % 5 != 0] 
print(list)

#What is the output of the following code examples?

#output 1:

TypeError: 'int' object is not iterable

#output 2:
SyntaxError: 'break' outside loop

#output 3
Endless loop of number 0

#Ex-8
for a in range(6):
    if (a == 3 or a==6):
        continue
    print(a,end=' ')
print("\n")

#Ex-9
number = input("Guess the lucky number : ")
while number != 5:
   print ("That is not the lucky number")
   number = input("Guess the lucky number ")
   #modification
number = -1
again = "yes"
while number != 5 and again != "no":
    number = input("Guess the lucky number: ")
    if number != 5:
        print ("That is not the lucky number")
        again = raw_input("Would you like to guess again? ")


# Ex-10
counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number :")
   if number != 5:
       print ("Try again.")
   else:
       print ("Good guess!")
       counter = counter +1
else:
   print ("Game over!")
   
# while statement with the counter and break (Ex:11)

counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print ("Try again.")
   else:
       print ("Good guess!")
       break
   counter = counter +1
else:
   print ("Sorry but that was not very successful")
