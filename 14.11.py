# Erick Jimenez
# PSID 1463639
# Zylab 14.11

# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(nmbrlst):
    for i in range(len(nmbrlst) - 1):
        index = i
        for j in range(i + 1, len(nmbrlst)):
            if nmbrlst[j] > nmbrlst[index]:
                index = j
        nmbrlst[i], nmbrlst[index] = nmbrlst[index], nmbrlst[i]
        print(' '.join([str(x) for x in nmbrlst]))

    return nmbrlst


if __name__ == '__main__':
    nmbr = [int(x) for x in input().split()]
    selection_sort_descend_trace(nmbr)