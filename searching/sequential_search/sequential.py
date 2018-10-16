def seq_search(arr, ele):
    pos = 0
    while pos < len(arr):
        if arr[pos] == ele:
            return pos
        else: 
            pos += 1


print(seq_search([0,4,2,7,4,10, 1], 1))