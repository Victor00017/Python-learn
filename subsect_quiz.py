# # # # Question 3: Create a program with a for loop and a break statement. 
# # # # The program should iterate over characters in an email address,
# # # # exit the loop when it reaches the @ symbol, 
# # # # and print the part before @ 
# # # # on one line. Use the skeleton below.
# # # #for ch in "john.smith@pythoninstitute.org"
# # # #    if ch == "@":
# # #         # Line of code.
# # #     # Line of code.
# # # email= input("Enter your email address ")
    
# # # for ch in email:
# # #     if ch=="@":
# # #         break
# # #     print(ch, end="") 
# # #    # Expected output: john.smith

# # # # Question 4: Create a program with a for loop and a continue statement.
# # # # The program should iterate over a string of digits, replace each 0 with x, 
# # # # and print the modified string to the screen. 
# # # # Use the skeleton below:

# # # for digit in "0165031806510":
# # #     if digit == "0":
# # #         print("x", end="")
# # #         continue
    
# # #     print(digit, end="")
        
# #     # Question 5: What is the output of the following code?

# # n = 3
 
# # while n > 0:
# #     print(n + 1)
# #     n -= 1
# # else:
# #     print(n)

# # Question 6: What is the output of the following code?

# n = range(4)
 
# for num in n:
#     print(num - 1)
# else:
#     print(num)

#Question 7: What is the output of the following code?

# for i in range(0, 6, 3):
#     print(i)
# Question 2: What is the output of the following snippet?


# x = 4
# y = 1
 
# a = x & y
# b = x | y
# c = ~x  # tricky!
# d = x ^ 5
# e = x >> 2
# f = x << 2
 
# print(a, b, c, d, e, f)
# 3.4.2 Indexing lists
# How do you change the value of a chosen element in the list?

# Let's assign a new value of 111 to the first element in the list. We do it this way:


numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.
#And now we want the value of the fifth element to be copied to the second element ‒ can you guess how to do it?


numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.
 
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
del numbers[1]
print(len(numbers))
print(numbers)