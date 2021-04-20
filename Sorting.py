import math


class Sorting:

    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        # O(n^2)Time[best case O(n)] and O(1)space
        is_sorted = False
        counter = 0
        while not is_sorted:
            is_sorted = True
            for i in range(len(self.array) - 1 - counter):
                if self.array[i] > self.array[i + 1]:
                    self.swap(i, i + 1)
                    is_sorted = False
            counter += 1
        return self.array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def heap_sort(self):
        self.build_max_heap()

    def build_max_heap(self):
        # To build max heap this algorithm takes O(nlog(n))
        # and O(1) Space
        pass
        for i in range(1, len(self.array)):
            track = i
            while self.array[math.floor((track-1)/2)] < self.array[track]:
                self.swap(math.floor((track-1)/2), track)
                track = math.floor((track-1)/2)
                if self.array[math.floor((track-1)/2)] > self.array[track] or track == 0:
                    break


a = [12, 4, 8, 12, 13, 3, 6, 7, 14, 2, 5]
sorting = Sorting(a)
# sorted_array = sorting.bubble_sort()
# print(sorted_array)
print(sorting.build_max_heap())
