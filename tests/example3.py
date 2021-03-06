# -*- coding: utf-8 -*-
from superior import superior, superiorMRO

class A(object):
    def __init__(self):
        print("A", end=" ")
        superior(A, self, "__init__")

class B(object):
    def __init__(self):
        print("B", end=" ")
        superior(B, self, "__init__")

class N(object):
    def __init__(self):
        print("N", end=" ")
class M(object):
    def __init__(self):
        print("M", end=" ")

class F1(A,N):
    def __init__(self):
        print("F1", end=" ")
        superior(F1, self, "__init__")
class F2(B,M):
    def __init__(self):
        print("F2", end=" ")
        superior(F2, self, "__init__")
        
class G(F1,F2):
    def __init__(self):
        print("G", end=" ")
        superior(G, self, "__init__")


def test(cl):
    print("MRO (super):", [x.__name__ for x in cl.__mro__])
    print("MRO (superior):", [x.__name__ for x in superiorMRO(cl)])
    print("Calls:", end=" ")
    cl()
    print()

test(G)