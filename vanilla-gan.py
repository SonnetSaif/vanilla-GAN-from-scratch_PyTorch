import argparse
import os
import numpy as np
import math

import torchvision.transforms as transforms
from torchvision.utils import save_image

from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable

import torch.nn as nn
import torch.nn.functional as F
import torch

os.makedirs('output', exist_ok=True)

img_shape = (1, 28, 28)

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.fc1 = nn.Linear(100, 128)
        self.fc2 = nn.Linear(128,512)
        self.fc3 = nn.Linear(512,1024 )
        self.fc4 = nn.Linear(1024,28*28)
        self.bn1 = nn.BatchNorm1d(128)
        self.bn2 = nn.BatchNorm1d(512)
        self.bn3 = nn.BatchNorm1d(1024)

    def forward(self, x):
        x = F.leaky_relu(self.bn1(self.fc1(x)),0.2)
        x = F.leaky_relu(self.in2(self.fc2(x)),0.2)
        x = F.leaky_relu(self.in3(self.fc3(x)),0.2)
        x = F.tanh(self.fc4(x))
        return x.view(x.shape[0],*img_shape)



class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc1 = nn.Linear(28*28, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128,1)

    def forward(self, x):
        x = x.view(x.size(0),-1)
        x = F.leaky_relu( self.fc1(x),0.2)
        x = F.leaky_relu(self.fc2(x),0.2)
        x = F.leaky_relu(self.fc3(x),0.2)
        x = F.sigmoid(self.fc4(x))
        return x
