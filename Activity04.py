# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 19:22:46 2022
@author: LENOVO
"""
#Linear search
def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)
    
#binary search
#1.Iterative binary search    
def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
       
        mid = (high + low) // 2  
   
        if list1[mid] < n:  
            low = mid + 1  
   
        elif list1[mid] > n:  
            high = mid - 1  

        else:  
            return mid  
        
    return -1  
  
  
# Initial list1  
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 45  
  
# Function call   
result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")  
    
#2.recursive binary search
def binary_search(list1, low, high, n):   
   
   if low <= high:  
  
      mid = (low + high) // 2  
  
      
      if list1[mid] == n:   
        return mid   
    
      elif list1[mid] > n:   
         return binary_search(list1, low, mid - 1, n)   

      else:   
         return binary_search(list1, mid + 1, high, n)   
  
   else:   

      return -1  
   
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 32  
  
# Function call   
res = binary_search(list1, 0, len(list1)-1, n)   
  
if res != -1:   
   print("Element is present at index", str(res))  
else:   
   print("Element is not present in list1")  