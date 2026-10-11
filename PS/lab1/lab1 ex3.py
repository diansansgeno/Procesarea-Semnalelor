# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:16:30 2026

@author: Lenovo
"""

fe = 2000 #nr esantioane

print ("Timpul intre doua esantioane este: ", 1/fe, " secunde.")
print()

#o ora are 3600 de secunde si avem 2000 x 3600 = 7.200.000 de esantioane pe ora
#apoi avem pentru 4 biti deci 28.800.000 de esantioane per bit per ora, si un byte are 8 biti deci impartim ce avem pana acum la 8
#ca sa obtinem bytes per ora de achizitie ->  3.600.000

#deci intr o ora de achizitie o sa avem 3.600.000 de bytes.

print ("Nr de bytes intr o ora de achizitie este 3.600.000 bytes.")