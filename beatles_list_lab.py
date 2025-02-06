# 3.4.11   LAB   The basics of lists ‒ the Beatles
# Scenario
# The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

# The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).


# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
# By the way, are you a Beatles fan? (The Beatles is one of Greg's favorite bands. But wait...who's Greg...?

# step 1
beatles=[]
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul MaCartney")
beatles.append("George harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    label=input("Enter the following names Stu Sutcliffe and Pete Best ")
    beatles.append(label)
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

#Question 2: What is the output of the following snippet?


# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0
 
# for number in lst:
#     add += number
#     lst_2.append(add)
 
# print(lst_2) 
# 

# The concept is rather simple ‒ we temporarily assume that the first element is the largest one, and check the hypothesis against all the remaining elements in the list.

# The code outputs 17 (as expected).

# The code may be rewritten to make use of the newly introduced form of the for loop:


# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
 
# for i in my_list:
#     if i > largest:
#         largest = i
 
# print(largest)
 
# The program above performs one unnecessary comparison, when the first element is compared with itself, but this isn't a problem at all.

# The code outputs 17, too (nothing unusual).

# If you need to save computer power, you can use a slice:


# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
 
# for i in my_list[1:]:
#     if i > largest:
#         largest = i
 
# print(largest)
 
# The question is: which of these two actions consumes more computer resources ‒ just one comparison, or slicing almost all of a list's elements?

# Now let's find the location of a given element inside a list:


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
 
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
 
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")
 
# Note:

# the target value is stored in the to_find variable;
# the current status of the search is stored in the found variable (True/False)
# when found becomes True, the for loop is exited.
# Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.

# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.

# The question is: how many numbers have you hit?

# This program will give you the answer:


# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
 
# for number in bets:
#     if number in drawn:
#         hits += 1
 
# print(hits)
 
# Note:

# the drawn list stores all the drawn numbers;
# the bets list stores your bets;
# the hits variable counts your hits.
# The program output is: 4