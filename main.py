import logging

import torch

from model import UNet
from operations import inference
from utils import load_sequence

# config
device = "cuda" if torch.cuda.is_available() else "cpu"
model_file = "models/unet.pth"

# prepare the model
model = UNet()
model = model.to(device)
model = torch.compile(model)

# load the model
checkpoint = torch.load(model_file)
model.load_state_dict(checkpoint["model"])
model.eval()

# load the image sequence
loader = load_sequence()

inference(model, loader, device)
