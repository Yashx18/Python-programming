"""firstName = int(input("Enter your name here : "))
age = 20
userName = "ken"

print(firstName, age, userName)

num1 = int(input('Enter First Number:'))
num2 = int(input('Enter Second Number:'))

print('Sum is',num1 + num2)

side = float(input('Enter side of square:'))
print('Area of square is ',side * side)

num1 = float(input('Enter first number :'))
num2 = float(input('Enter second number :'))

name = 'Hello $my name $is yash $and i $am 20 years old'
print(name.count('$'))

marks = int(input('Enter your Marks :'))

if(marks >= 90):
    print('Grade A')
elif(marks <90 and marks >= 80):
    print('Grade B')
elif(marks < 80 and marks >= 70):
    print('Grade C')
elif(marks < 70 and marks >= 60):
    print('Grade D')
else:
    print('You have Failed')

num = int(input("Enter number :"))
res = num % 2

if( res == 0 ):
    print(num,'is Even')
else:
print((num1 + num2)/2)
    print(num,'is Odd')


num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if(num1 > num2 and num1 > num3):
    print(num1,'is the Greatest of all numbers')
elif(num2 > num1 and num2 > num3):
    print(num2,'is the Greatest of all numbers')
elif(num3 > num1 and num3 > num2):
    print(num3,'is the Greatest of all numbers')

num = int(input("Enter number :"))
if((num % 7 ) == 0):
    print(num,'is divisible by 7')
else:
    print(num,'is not divisible by 7')

marks = [1,2,3,4,5,6]
print(marks)
print(type(marks))
print(len(marks))

numbers = [23, 7, 45, 12, 89, 34, 66, 18, 91, 5]

print(numbers[0:4])
#numbers[0] = 'Yash' # To update value in List
print(numbers)

# numbers is a List.
numbers = [23, 7, 45, 12, 89, 34, 66, 18, 91, 5]
numbers.append(10)# Adds the value at the end of the List.{similar to Push in JavaScript}. Output = [23, 7, 45, 12, 89, 34, 66, 18, 91, 5, 10] 'Value added at the end'
numbers.sort()# Rearranges the values of List in 'Ascending' order(By Default) and makes changes directly into the original List. Output = [5, 7, 10, 12, 18, 23, 34, 45, 66, 89, 91]
print(numbers)# Prints the whole list as it is.
numbers.sort(reverse=True)# Rearranges the values of List in 'Descending' order(By adding 'reverse=true') and makes changes directly into the original List. Output = [91, 89, 66, 45, 34, 23, 18, 12, 10, 7, 5]
print(numbers)# Prints the whole list as it is.
fruits = ['banana', 'apple', 'orange','dragon fruit']
fruits.sort()# Sorting also works on strings and chars.
alphabets = [1,2,3,4,5,1,2,3,4,5]
# alphabets.reverse()# This reverse method just reverses the whole list as it is and directly changes the original list.
alphabets.insert(0, 0)# This insert method is used to enter the element at a specific index and shifts the other values. syntax: .insert(index, element).Changes the original list.
print(alphabets)

l1 = [2,1,3,1]
#l1.remove(1)# This method removes the first occuerence of element like [2,1,3,1], In this example it will remove the first 1.Output = [2, 3, 1]
l1.pop(2)# This pop method removes the element at a specific index. Output = [2, 1, 1]
print(l1)
"""

"""
LIST IS A MUTABLE DATA TYPE ,
TUPLE IS AN IMMUTABLE DATA TYPE IN PYTHON.
Mutable -> can be changed
Immutable -> can not be changed
"""
"""
num = (1,2,3,4,2)# This is a tuple with multiple values but to create a single value tuple, the syntax is as follows.
num2 = (1,)# Comma is necessary otherwise the python will consider it as int or the type of value entered.
print(num.index(2))# It returns the index of first occurence like num.index(2) Output : 1.
print(num.count(2))# It counts the total occurences of element in tuple num.index(2) Output = 2.

print(num)# Slicing works as same as list in the tuples.
# print(num2)

# print(type(num))
"""

# favoriteMovies = []
# for i in range(3):
#     movieName = str(input("Enter name of favorite movie :"))
#     favoriteMovies.append(movieName.strip())


# print(favoriteMovies)

# listEl = [1,2,3,2,1]
# reversedList = listEl.copy()
# reversedList.reverse()
# # print(reversedList)
# if (listEl == reversedList):
#     print('Palindrome')
# else:
#     print('Not Palindrome')

# grades = ['C','D','A', 'A', 'B', 'B', 'A']
# print('Number of Students with Grade A is',grades.count('A'))

# sortedGrades = grades.copy()
# sortedGrades.sort()
# print(sortedGrades)

# info = {
#     'name': 'ken',
#     'age': 20,
#     "learning": ['Python', 'MERN'],
#     'isMale': True,
#     'full name': 'Ken Yeager'
# }
# info['name']='Ken'
# print(info['name'])
# print(info)

# null_dict = {}

# null_dict['userName']='kenx024'
# null_dict['programmingLanguages']={
#     'Web2': 'JS/TS',
#     'Web3': 'solidity/rust',
#     'general': 'Python'
# }

# print(null_dict)

# Nested Dictionary
ken = {
    "programmingLanguages": {
        "Web2": "JS/TS",
        "Web3": "solidity/rust",
        "general": "Python",
    },
    "age": 20,
}

# print(ken)
# print(ken['programmingLanguages']['Web2'])

# print(list(ken.keys()))
# print(list(ken.values()))
# print(list(ken.items()))

# print(ken)
# ken.update({'city': 'Delhi'})
# print(ken)

# Set does not store duplicate values and not even counted no moatter what language.
collection = {1, 2, 2, 2, 3, 4, "hello"}
# print(type(collection))
# print(len(collection))

# Empty Set
# Note : Sets itself are mutable but the elements of sets are immutable.
newSet = set()

newSet.add(1)
newSet.add(2)
newSet.add(3)

newSet.remove(3)

newSet.add("hi")
newSet.add((1, 2))
# Lists and Dictionary can not be added into set.
# Unhashable = list and dictionaries etc.

# print(len(newSet))
# newSet.clear() # Clears the whole set.
newSet.pop()  # Removes a random value from the Set.
# print(newSet)
# print(len(newSet))


set1 = {1, 2, 3}
set2 = {2, 3, 4}

# print(set1.union(set2))# Combines both set values and returns a new seat and common values are only considered only once.

# print(set1.intersection(set2))# Combines common values and returns new set with only duplicate values.

meanings = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal",
}
# print(list(meanings.items()))

subjects = {
    "python",
    "python",
    "python",
    "java",
    "java",
    "java",
    "C++",
    "C++",
    "javascript",
    "C",
}
# print(subjects)
# print(len(subjects))

# result = {}
# for i in range(3):
#     subject = str(input('Enter Subject :'))
#     marks = float(input('Enter Marks :'))
#     result[subject] = marks

# print(result)

num = {("int", 9), ("float", 9.0)}
# print(num)

# list1 = ['a','b','c','d','e','f','g','h']
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# num = int(input('Enter Number :'))
# i = 1
# while i <= 10:
#     print(num * i)
#     i += 1;

# arr = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(arr):
#     print(arr[i])
#     i += 1;

arr = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input('Enter number to find :'))
# i = 0
# while i < len(arr):
#     if (arr[i] == x):
#         print(x,'found at Index :',i)
#         break

#     i += 1;


# for x in arr:
#     print(x)

# num = int(input('Enter number :'))
# for x in arr:
#     if (x == num):
#         print(num,'found at index', arr.index(x))

# for i in range(1,11,2): # range(start,stop,step)
#     print(i)

# for i in range(101):
#     print(i)


# for i in range(100, 0, -1):
#     print(i)

# num = int(input('Enter number :'))

# for i in range(1,11):
#     print(num * i)

# for i in range(5):
#     #empty
#     pass # Pass is used to not get any work done like null statement.

# print('some work done')


# sum = 0;
# num = int(input("Enter Number :"))

# limit = num + 1
# for i in range(1,limit):
#     sum += i
# print(sum)

# i = 1
# while (i <= num):
#     sum += i;
#     i += 1
# print(sum)


# i = 1
# while (i <= num):
#     sum += i;
#     i += 1
# print(sum)

# n = 1
# limit = int(input('Enter a Natural Number :'))
# newLimit = limit + 1
# for i in range(1,newLimit):
#     n *= i
# print('Factorial of',limit,'is',n,'.')


###################### Functions and Recursions #####################

# def sum(a,b):
#     return a + b

# ans1 = sum(2,2)
# print(ans1)

# print(sum(2,2))

# def avg(a,b,c):
#     return (a+b+c)/3

# ans = avg(2,3,5)
# print(ans)

# def length(list):
#     return len(list)

# ans = length([1,2,3,4,5,6,7,8,9,10])
# print(ans)

# def elments(list):
#     for i in list:
#         print(i)

# ans = elments([1,2,3,4,5,6,7,8,9,10])
# print(ans)


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# print(factorial(4))

# def converter(amt):
#     return amt * 86.377

# ans = converter(10)
# print(ans)


def identifier(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# num = int(input("Enter Number :"))
# identifier(num)

# RECURSION => When a function calls itself repeatedly.(Like a loop and loops and recursions can be used interchangeably)


# def show(num):
#     if (num == 0):# this step is called 'Base Case'.
#         return
#     print(num)
#     show(num - 1)


# show(5)


# def fact(n):
#     if n == 0 or n == 1:
#         return 1

#     return n * fact(n - 1)

# print(fact(4))

# def sum(n):
#     if n == 0 :
#         return 0

#     return n + sum(n - 1)

# print(sum(5))


def printElements(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    printElements(list, idx + 1)


# printElements([1,2,3,4,5,6])

#############File Input/Output in Python #############

"""
'r' : open for reading(default)
'w' : open for writing, truncating the file first.(Data will be deleted and overwritten)
'x' : creates a new file and open it for writing
'a' : open for writing, appending to the end of the file if it exists
'b' : binary mode
't' : text mode (default)
'+' : open a disk file for updating (reading or writing)

"""

# f = open("demo.txt", "r+")# It overwites the file from the starting point at first line.
# data = f.read()
# data = f.read(5)
# line1 = f.readline()
# line2 = f.readline()
# print(data)
# print(type(data))
# print(line1)
# print(line2)
# f.close()


# updatedFile = f.write('\nthis file has appended data.')
# print(updatedFile)
# f.write('YO Buddies')
# print(f.read())
# f.close()

# with open('new.txt','r') as f:
#     print(f.read())

# with open("new.txt", "w") as f:
#     f.write("yo")

# import os
# os.remove('new.txt')


def find(file, word):
    with open(file, "r") as f:
        data = f.read()
    if word in data:
        print("Found")
    else:
        print("Not Found")


# find('practice.txt', 'learning')

# newData = data.replace('Java','Python')
# print(newData)


def checkForLine(word):
    data = True
    line = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(word, "found at line", line)
                break
            else:
                line += 1

    return -1


# checkForLine('File')

with open("nums.txt", "r") as file:
    count = 0
    evenList = []
    nums = ""
    for line in file:
        items = line.strip().split(",")
        nums = items
    for i in nums:
        num = int(i)
        # print(i)
        res = num % 2
        if res == 0:
            count += 1
            evenList.append(num)
    print("Even numbers List :", evenList)
    print("Count :", count)

    #     if(items % 2 == 0):
    #         count += 1

    # print(count)
