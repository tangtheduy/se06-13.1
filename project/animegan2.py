import torch 
from typing import Union, List
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def run(path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", device=device).eval()
    face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", size=512)

    img = Image.open(path)
    out = face2paint(model, img)
    return out
