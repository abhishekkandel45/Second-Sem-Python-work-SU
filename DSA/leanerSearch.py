
def linerSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
\

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = int(input("Enter the key to search: "))
index = linerSearch(arr, key)
if index == -1:
    print("Key not found")
else:
    print("Key found at index: ", index)