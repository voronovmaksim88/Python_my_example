class Counter:
    def __init__(self, start=0):
        self.count = start

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0


my_counter = Counter()
my_counter.inc()
my_counter.inc()
my_counter.inc()
print(my_counter.count)
my_counter.reset()
print(my_counter.count)
