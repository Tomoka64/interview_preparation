def binary_search(arr, ele):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = int((first+last) / 2)
        if arr[mid] == ele: 
            return mid
        else:
            if arr[mid] > ele:
                last = mid - 1
            else:
                first = mid + 1

def rec_binary_search(arr, ele, pos=0):
    if len(arr) == 0: return None
    else:
        mid = int(len(arr) / 2)
        if arr[mid] == ele:
            return pos + mid
        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid], ele, pos)
            else:
                pos += mid
                return rec_binary_search(arr[mid:], ele, pos)

print(rec_binary_search([1,2,3,4,5,6,7,8,9],9))