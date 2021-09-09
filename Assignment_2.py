#TASK THREE DATA STRUCTURES

1. Create a list of 10 elements of four different data types like int, string, complex and float.
ls = ["abc", 123 ,123.0 ,2 + 2j]

2. Create a list of size 5 and execute the slicing structure
ls = ["abc", 123 ,123.0 ,2 + 2j, 123]
print(ls[::])
print(ls[-5::])
print(ls[0::])
print(ls[0:3:])

3. Write a program to get the sum and multiply of all the items in a given list.

def multiply(ls):
    sum=1
    for x in ls:
        sum=sum*x
    return sum;

def add(ls):
    sum=0
    for x in ls:
        sum=sum+x
    return sum;


print(multiply([1,2,3,4,5]))
print(add([1,2,3,4,5]))


4. Find the largest and smallest number from a given list.
print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))

5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
ls = [1,2,3,4,5,6,7,8,9]
print([x for x in ls if x%2==0 ])

6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
ls = list(range(1, 31))
print([i*2 for x,i in enumerate(ls) if x < 6 or x > 24])

7. Write a program to replace the last element in a list with another list.
 Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]

ls1,ls2 =[1,3,5,7,9,10], [2,4,6,8]
print(ls1)
print(ls2)
ls1.pop(len(ls1)-1)
ls1.extend(ls2);
print(ls1)



8. Create a new dictionary by concatenating the following two dictionaries:

Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

print(merge_two_dicts(a,b));



9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).

Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

def create_dicts(n):
    c={i:i*i for i in range(1,n+1)}
    return c
print(create_dicts(10))


10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

s='34,67,55,33,12,98'
print(s.split(','))
print(tuple(s.split(',')))


#Task-4

1. Write a program to reverse a string. Sample input: “1234abcd” Expected output: “dcba4321”

print("1234abcd"[::-1])

2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12


def count(s):
    lwrcnt=0
    uprcnt=0
    for i in s:
        if i.islower():
            lwrcnt=lwrcnt+1
        else:
            uprcnt=uprcnt+1
    return "No. of Uppercase characters : "+ str(uprcnt) + "\nNo. of Lower case Characters : "+ str(lwrcnt)

print(count("abcSdefPghijQkl"))




3. Create a function that takes a list and returns a new list with unique elements of the first list

ls = [1, 2, 3, 1, 2, 5, 6, 7, 8]
print(list(set(ls)))

4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.
ls = "Nirav-Rami-ABC".split("-")
print(sorted(ls))


5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Sample input: Hello world Practice makes man perfect
Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

s= "Hello world Practice makes man perfect"
print(s.upper())


6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
def add(a , b) :
    return int(a) + int(b)
print(add("2", "7"))


 7. Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function should print both the strings line by line.
 def maxLength(a , b) :
    al = len(a)
    bl = len(b)
    if(al==bl):
        return a+"\n"+b
    elif(al > bl):
        return a
    else:
        return b
print(maxLength("abc", "qwe"))


8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
def squares(n) :
    return tuple([x*x for x in range(1,n+1)])

print(squares(20))

9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.

Sample input: show Numbers(3) (where limit=3) Expected output:
0 EVEN 1 ODD 2 EVEN 3 ODD

def identifyEvenOrOdd(n):
    return ''.join([str(x) + ' EVEN ' if x%2==0 else str(x) + " ODD " for x in range(1,n+1)])

print(identifyEvenOrOdd(20))


10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)

def identifyEvenOrOdd(n):
    return n%2==0

print(list(filter(identifyEvenOrOdd, range(1,21))))

11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the numbers in the filtered list. Use lambda() to define anonymous functions.

print(list(map(lambda x: x*x ,filter(lambda n:n%2==0, range(1,11)))))


 12. Write a function to compute 5/0 and use try/except to catch the exceptions
try :
    x=5/0
except Exception as e:
    print(e)



13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
print(reduce(lambda x,y:str(x)+str(y) , range(1,8)))

14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.

print(list(filter(lambda n:n%3!=0 ,filter(lambda n:n%7==0, range(1,100)))))


15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
ls = [7 ,5 ,6 ,1, 2]
print(list(map(lambda x : x*x ,ls)))

16. What is the output of the following codes: (i) def foo():
a ) 2
b) after f
after f?
NameError: name 'f' is not defined
