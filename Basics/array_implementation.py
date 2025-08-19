"""
Array Implementation using python

Arrays are not native to python.
An array is a data structure, consists of a collection of elements, Where each element posses an identity index.
In short the location of element can be found by knowing the right index(key).
Python is dynamically typed language, which means that we need not define the size of the array before.
Arrays are handy over other data types,like linked list that are used to store elements over fact that most of the
array operations offers Big O of 1
"""
import ctypes


# Let's implement append(), delete(), list() and __getitem__(), len() operations on your python array.

class ArrayImp():
    def __init__(self):
        self.item_count = 0
        self.array_capacity = 1
        self.primary_array = self._create_array(self.array_capacity)

    def _create_array(self, size):
        #creates new array with input capacity
        return (size * ctypes.py_object)()

    def list(self):
        #list element of array
        for item in self.primary_array:
            return "".join(str(self.primary_array[x]) for x in range(self.item_count))

    def __len__(self):
        #Returns the number of items in an array
        return self.item_count

    def __getitem__(self, item_index):
        # Return item at index k
        if not 0 <= item_index< self.item_count:
            return IndexError('index out of range')
        return self.primary_array[item_index]



array_object = ArrayImp()
array_object.list()