
def bubblesort_once(l):
    # create a shallow copy of the list
    res = l[:]

    for i in range(0, len(res) - 1):
        if res[i] > res[i + 1]:
            temp = res[i]
            res[i] = res[i + 1]
            res[i + 1] = temp

    return res

my_list = [9, 7, 5, 3, 1, 2, 4, 6, 8]

print(bubblesort_once(my_list))

