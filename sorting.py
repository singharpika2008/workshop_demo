# sort the list using sliding window/bubble sort
def bubble_sort(arr):

    a = len(arr)

    for i in range(a-1):
        for j in range(a-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        return(arr)        
print(bubble_sort([5,9,6,23,7]))
