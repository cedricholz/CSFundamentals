# Insertion, Delete: O(log(n)
class MinHeap:

    def __init__(self):
        self.h = []
        self.last_index = -1

    def push(self, val):
        if self.last_index == -1:
            self.h.append(val)
            self.last_index = 0
        else:
            self.last_index += 1
            if len(self.h) - 1 < self.last_index:
                self.h.append(val)
            self.h[self.last_index] = val

        cur_index = self.last_index
        parent_index = int((cur_index - 1) / 2)

        while self.h[parent_index] > val:
            self.h[parent_index], self.h[cur_index] = self.h[cur_index], self.h[parent_index]
            parent_index, cur_index = int((parent_index - 1) / 2), parent_index

    def sink(self):

        cur_index = 0
        left_child_index = 2 * cur_index + 1
        right_child_index = 2 * cur_index + 2

        while left_child_index < len(self.h) or right_child_index < len(self.h):
            left = False
            right = False
            if left_child_index < len(self.h) and right_child_index < len(self.h):
                if self.h[left_child_index] < self.h[right_child_index]:
                    left = True
                else:
                    right = True
            elif left_child_index < len(self.h):
                left = True
            else:
                right = True
            if left:
                self.h[cur_index], self.h[left_child_index] = self.h[left_child_index], self.h[cur_index]
                cur_index = left_child_index
            elif right:
                self.h[cur_index], self.h[right_child_index] = self.h[right_child_index], self.h[cur_index]
                cur_index = right_child_index
            left_child_index = 2 * cur_index + 1
            right_child_index = 2 * cur_index + 2

    def pop(self):
        r = self.h[0]
        self.last_index -= 1
        self.h[0] = self.h.pop()
        self.sink()
        return r
