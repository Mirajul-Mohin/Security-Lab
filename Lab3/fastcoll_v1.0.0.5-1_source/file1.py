#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ���uF��TֵM���wX,����
!�{��!!���^���"��4��kf�FI��!�Y葦>�ĲY�f쥙1=�rg���j�5�����F�o.f�����Q7�J�l�N4z,�)�qOf�
9"""
from hashlib import sha256
print sha256(blob).hexdigest()
