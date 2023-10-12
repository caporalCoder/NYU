#
# Problem statement:
#
# Without using the max() function in python, create a function that returns the max value using:
#
#  * recursion.
#
#  * a pivot that splits the list in half.
#
#

def recursive_max(lst):
    """
    Finds the maximum value in a list using recursion by splitting the list in half.

    Args:
    - lst (list): The list of numbers.

    Returns:
    - int/float: The maximum value in the list.
    """

    # Base case: If the list is empty, return a very small number (can also use float('-inf')).
    if not lst:
        return float('-inf')

    # Base case: If there's only one element, return that element.
    if len(lst) == 1:
        return lst[0]

    # Find the pivot to split the list.
    pivot = len(lst) // 2

    # Recursively find the maximum in the left and right halves.
    max_left = recursive_max(lst[:pivot])
    max_right = recursive_max(lst[pivot:])

    # Return the larger of the two maximums.
    if max_left > max_right:
        return max_left
    else:
        return max_right

# Test case.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 30, 3, 5]
print(recursive_max(numbers))  # Expected output: 30
