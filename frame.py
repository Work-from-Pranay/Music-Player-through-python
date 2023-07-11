import tkinter as tk
from PIL import Image

file='22H.gif'

info=Image.open(file)
frames=info.n_frames
print(frames)