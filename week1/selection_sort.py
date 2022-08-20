#User function Template for python3

class Solution:
    def selectionSort(self, arr,n):
        for i in range(0, n - 1 ):
            min = i
            for j in range(i, n):
                if arr[j] < arr[min]:
                    min = j
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
