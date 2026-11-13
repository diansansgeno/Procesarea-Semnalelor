# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:02:57 2026

@author: Lenovo
"""

import numpy as np

P_semnal_dB = 90
SNR_dB = 80

P_zgomot_dB = P_semnal_dB - SNR_dB
print("P_zgomot =", P_zgomot_dB, "dB")

P_s = 10 ** (P_semnal_dB / 10)
P_z = 10 ** (P_zgomot_dB / 10)
print("P_semnal =", P_s)
print("P_zgomot =", P_z)
print("raport =", P_s / P_z)
print("SNR =", 10 * np.log10(P_s / P_z), "dB")