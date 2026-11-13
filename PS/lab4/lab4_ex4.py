# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:02:54 2026

@author: Lenovo
"""

import math

fL = 40      
fH = 200     
B = fH - fL  

n = math.floor(fH / B)
fs_min = 2 * fH / n

print("B =", B, "Hz")
print("n = floor(fH/B) =", n)
print("fs_min =", fs_min, "Hz")
print("Practic: fs >", fs_min, "Hz")

def frecventa_alias(f, fs):
    f = f % fs
    if f > fs / 2:
        f = fs - f
    return f

for fs in [320, 400, 440]:
    fa = frecventa_alias(200, fs)
    print(f"fs = {fs} Hz -> 200 Hz ajunge la {fa} Hz")