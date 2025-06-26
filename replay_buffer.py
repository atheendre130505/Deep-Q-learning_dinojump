import numpy as np
class replay_buffer:
    def __init__(self,capacity):
        self.capacity = capacity
        self.buffer = []
        self.index = 0
    def add(self,new):
        if len(self.buffer) < self.capacity:
            self.buffer.append(new)
        else:
            self.buffer[self.index] = new
            self.index = (self.index + 1) % self.capacity
    
    def sample(self, batch_size):
        indices = np.random.choice(len(self.buffer), batch_size, replace=False)
        return [self.buffer[i] for i in indices]
    
    def __len__(self):
        return len(self.buffer)