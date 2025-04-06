
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

grades = ['C','D','A', 'A', 'B', 'B', 'A']
print('Number of Students with Grade A is',grades.count('A'))

sortedGrades = grades.copy()
sortedGrades.sort()
print(sortedGrades)