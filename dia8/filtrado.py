"""
a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i] for i in range(n))
print(filtered_array)
"""

a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array2 = [a [i] for i  in range(n) if a[i]<1000]
