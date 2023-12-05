# Given a
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3
# Binary search will split this dara into half
# Get the first index and rhe last index and add it together and then divide it by twp
# (o+9) / 2
"""
1: A function that takes a list and target parameter
2: Multiple variables : middle, start, end, steps
3: recursion or while loop
4: Increases the steps each time a split is done
5: conditions to track target position


"""


def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    # set up a loop for repetition
    while start <= end:
        # convert list to string
        print("Step", steps, ":", str(list[start:end + 1]))

        # update steps
        steps = steps + 1
        middle = (start + end) // 2

        # check if element is equal to list
        if element == list[middle]:
            # return middle
            return middle
        # check if element is less than list
        elif element < list[middle]:
            # return end -1
            end = middle - 1

        else:
            # check if the element is greater than the target
            if element > list[middle]:
                # update the start to middle + 1
                start = middle + 1
    # if answer not found return - 1 and exit the loop
    return - 1


my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 9
print(binary_search(my_list, target))

"""
Lets use Binary search(searching through elements one by one)
and see the behaviour of our function
"""
for i in my_list:
    if i == 12:
        print(i)
"""
The draw back is the for Linear search, the function we count from
 index 0 - the last index to be able to print a value for us and 
 this is time consuming. worse case complexity
"""







