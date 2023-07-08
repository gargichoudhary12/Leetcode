class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.arr = [0] * m
        self.pos = m
        # Initialize lh1 of size k, rh1 of size m-k
        self.lh1, self.rh1 = self.heap_init(m, k)

        # Initialize lh2 of size m-k, rh2 of size k
        self.lh2, self.rh2 = self.heap_init(m, m - k)
        self.score = 0
        self.heap_size_cutoff = 2*m

    def heap_init(self, p1, p2):
        h1 = [(0, i) for i in range(p1 - p2, p1)]
        h2 = [(0, i) for i in range(p1 - p2)]
        return h1, h2

    def update(self, left_max_heap, right_min_heap, num):
        score = 0
        old_index = self.pos - self.m

        # If number to add belongs with upper k
        if num > right_min_heap[0][0]:

            # Check position of old, to delete number
            # If old number was not in right heap, rebalance by moving from right to left
            if self.arr[self.pos % self.m] <= right_min_heap[0][0]:
                if right_min_heap[0][1] >= old_index:
                    score += right_min_heap[0][0]

                score -= self.arr[self.pos % self.m]

                old_right_val, old_right_ind = heapq.heappop(right_min_heap)
                heapq.heappush(left_max_heap, (-old_right_val, old_right_ind))

            heapq.heappush(right_min_heap, (num, self.pos))
        else:

            score += num
            if self.arr[self.pos % self.m] >= right_min_heap[0][0]:
                # Move from left_max_heap to right_min_heap

                old_left_val, old_left_ind = heapq.heappop(left_max_heap)
                score += old_left_val
                heapq.heappush(right_min_heap, (-old_left_val, old_left_ind))

            else:
                score -= self.arr[self.pos % self.m]

            heapq.heappush(left_max_heap, (-num, self.pos))

        # lazy-deletion
        while left_max_heap and left_max_heap[0][1] <= old_index:
            heapq.heappop(left_max_heap)
        while right_min_heap and right_min_heap[0][1] <= old_index:
            heapq.heappop(right_min_heap)

        # Diligent deletion if heaps get too big
        if len(left_max_heap) > self.heap_size_cutoff:
            left_max_heap[:] = [(a, b) for a, b in left_max_heap if b > old_index]
            heapq.heapify(left_max_heap)

        if len(right_min_heap) > self.heap_size_cutoff:
            right_min_heap[:] = [(a, b) for a, b in right_min_heap if b > old_index]
            heapq.heapify(right_min_heap)

        return score

    def addElement(self, num):
        t1 = self.update(self.lh1, self.rh1, num)
        t2 = self.update(self.lh2, self.rh2, num)

        self.arr[self.pos % self.m] = num
        self.pos += 1
        self.score += (t2 - t1)

    def calculateMKAverage(self):
        if self.pos < 2 * self.m:
            return -1
        return self.score // (self.m - 2 * self.k)