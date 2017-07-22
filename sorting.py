#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    for item in range(len(lst)-1):
        made_swap = False

        for other_item in range(len(lst)-1-item):
            if lst[other_item] > lst[other_item + 1]:
                lst[other_item], lst[other_item + 1] = lst[other_item + 1], lst[other_item]
                made_swap = True

        if not made_swap:
            break

    return lst

def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    result = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(list1) and index_2 < len(list2):
        if list1[index_1] < list2[index_2]:
            result.append(list1[index_1])
            index_1 += 1
        else:
            result.append(list2[index_2])
            index_2 += 1

    # if there are still items in list1, even tho list2 is finished
    if index_1 < len(list1):
        result.extend(list1[index_1: ])

    # if there are still items in list2, even tho list1 is finished
    if index_2 < len(list2):
        result.extend(list2[index_2: ])

    return result


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    
    # I have the solution but I'm still not 100% on explaining each line, so
    # I'm not submitting an official answer. I'll will get there, soon. :)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
