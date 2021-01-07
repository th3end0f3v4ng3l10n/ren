import os
import sys
import random

text = ['oh','shit','here','we','go','again']
def ren():
    print(os.listdir())
    i = 0
    for file in os.listdir():
        os.rename(file, text[i])
        i+=1
ren()
