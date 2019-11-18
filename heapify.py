"""
Heap is a special tree structure in which each parent node is less than or equal to its child node.
Then it is called a Min Heap. If each parent node is greater than or equal to its child node then
it is called a max heap. It is very useful is implementing priority queues where the queue item
with higher weightage is given more priority in processing.

A heap is created by using python’s inbuilt library named heapq. This library has the relevant
functions to carry out various operations on heap data structure
"""
import heapq

# Creating a Heap
# A heap is created by simply using a list of elements with the heapify function.
# In the below example we supply a list of elements and the heapify function rearranges
# the elements bringing the smallest element to the first position.
H = [21, 1, 45, 78, 3, 5]
heapq.heapify(H)
print(H)

# Inserting into heap
# Inserting a data element to a heap always adds the element at the last index. But you
# can apply heapify function again to bring the newly added element to the first index
# only if it smallest in value. In the below example we insert the number 8.
heapq.heappush(H, 13)
print("Before Heapifying: {}".format(H))
heapq.heapify(H)
print("After Heapifying: {}".format(H))

# Removing from heap
# You can remove the element at first index by using this function. In the below example
# the function will always remove the element at the index position 1.
heapq.heappop(H)
print("After Popping: {}".format(H))

# Replacing in a Heap
# The heapreplace function always removes the smallest element of the heap and inserts
# the new incoming element at some place not fixed by any order.
heapq.heapreplace(H, 3)
print(H)