import numpy as np
a= np.random.uniform(0,11,size=20)
x=np.round(a,2)
print(x)
print(np.min(x),np.max(x),np.median(x))
for index,i in enumerate(x):
    if(i<5):
        x[index]=i*i
print(x)
def numpy_alternate_sort(array):
    sorted_array=np.sort(array)
    l=[]
    left = 0
    right = len(sorted_array) - 1
    while(left<=right):
        l.append(sorted_array[left])
        left += 1
        if left <= right:
            l.append(sorted_array[right])
            right -= 1
    return np.array(l)