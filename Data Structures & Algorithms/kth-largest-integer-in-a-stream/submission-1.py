class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        #so i can do like [-3] after do sorted() method.
        self.k = k
        self.arr = nums


    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        
        return self.arr[-self.k]



        
