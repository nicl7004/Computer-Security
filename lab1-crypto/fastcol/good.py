#!/usr/bin/python
# -*- coding: utf-8 -*-
good = "I come in peace."
evil = "Prepare to be destroyed!"
blob = """
               �?X����c�
T�Ր!#��z�-Dd���m&<����~�Q��ZS��eћ����L�\�3H|��%��?�_d�\�l��W0��X�/�7;����_a�A��n�����Т��&�l�Ё���q�)J"""
from hashlib import sha256
z = sha256(blob).hexdigest()
i = int(z, 16)
if(i%2 == 0):
  print(good)
else:
  print(evil)
