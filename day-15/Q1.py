# Program to reverse an array
n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Original array:", arr)

start = 0
end = n - 1
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start = start + 1
    end = end - 1

print("Reversed array:", arr)