#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ���uF��TֵM���wX,�����
!�{��!!���^���"��40�kf�FI��!+Y葦>�ĲY�f쥙1=�rg�����5�����F�o.f�����Q7��I�l�N4z,�)�q�f�
9"""
from hashlib import sha256
if (sha256(blob).hexdigest()=='b5234093784b654e877a304b24aa0c26a8f3d7d6e60e144b960982425337c53e'):
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")
