class RecentCounter:
    def __init__(self):
        self.records = deque()
  
    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[0] < t - 3000:
            self.records.popleft()
        return len(self.records)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)