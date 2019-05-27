# -*- coding: utf-8 -*-
from superior import superior, superiorMRO

class A(object):
    def __init__(self):
        print("A", end=" ")
        superior(A, self, "__init__")
    pass
    
class B(object):
    def __init__(self):
        print("B", end=" ")
        superior(B, self, "__init__")
    pass

# some other module defines this class, not knowing about super()

class C(A,B):
    def __init__(self):
        print("C", end=" ")
        A.__init__(self)
        B.__init__(self)
#        superior(D, self, "__init__")
    pass

print("MRO (super):", [x.__name__ for x in C.__mro__])
print("MRO (superior):", [x.__name__ for x in superiorMRO(C)])
print("Calls:", end=" ")
C()
print()