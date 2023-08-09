def last_element(lst):
    # """Return last item in list (None if list is empty.
    #
    #     >>> last_element([1, 2, 3])
    #     3
    #
    #     >>> last_element([]) is None
    #     True
    # """

    if lst == []:
        return None
    else:
        return lst[len(lst) - 1]


result = last_element([4,6,89,4,2,1])
print(result)