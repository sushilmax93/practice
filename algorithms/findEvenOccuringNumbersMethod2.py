# Find even occurring elements in an array of limited range
# Given an array that contains odd number of occurrences for all numbers except for a few elements which are present even number of times. Find the elements which have even occurrences in the array in O(n) time complexity and O(1) extra space.
# Assume array contain elements in the range 0 to 63.

# Examples :

# Input: [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
# Output: 12, 23 and 15

# Input: [1, 4, 7, 5, 9, 7, 3, 4, 6, 8, 3, 0, 3]
# Output: 4 and 7

# Input: [4, 4, 10, 10, 4, 4, 4, 4, 10, 10]
# Output: 4 and 10


# METHOD: 
# XOR THE INPUT NUMBERS AND THEN PRINT THEM 
# WHO HAVE EVEN FREQUENCIES


#find even occuring numbers function definition
def findEvenOccuringNumbers(arr):

    bits = [-1] * (max(arr) + 1)

    for ele in arr:

        if(bits[ele] == 1):
            bits[ele] = 0

        else:
            bits[ele] = 1


    print("This is array:-")
    print(arr)
    print("and these are even occuring numbers:- ")

    for i in range(len(bits)):
        if(bits[i] == 0):
            print(i)
    print("\n")        


#main function definition
if __name__=="__main__":
    list = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
    findEvenOccuringNumbers(list)

    list = [1, 4, 7, 5, 9, 7, 3, 4, 6, 8, 3, 0, 3]
    findEvenOccuringNumbers(list)

    list = [4, 4, 10, 10, 4, 4, 4, 4, 10, 10]
    findEvenOccuringNumbers(list)
