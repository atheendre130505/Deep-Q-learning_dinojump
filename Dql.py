import numpy as np
import torch 
import torch.nn as nn


class DQL(nn.Module):
    def __init__(self, input_size, output_size):
        super(DQL, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, output_size),
            nn.Softmax(dim=1)
        )
    def forward(self, x):
        return self.net(x)
    

    

        