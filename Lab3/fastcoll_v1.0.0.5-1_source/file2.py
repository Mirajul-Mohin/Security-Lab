#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ���uF��TֵM���wX,�����
!�{��!!���^���"��40�kf�FI��!+Y葦>�ĲY�f쥙1=�rg�����5�����F�o.f�����Q7��I�l�N4z,�)�q�f�
9"""
from hashlib import sha256
print sha256(blob).hexdigest()
