# -*- coding: utf-8 -*-
"""
see https://fuhm.net/super-harmful/ 
    - Example 1-2

Hierarchy diagram:

 -------------
 |  (object) |
 -------------
       |
       |
  -----------
  | OBJECT  | <-- included so we can prove it is called only ONCE
  -----------
     /   \
    /     \
-----     -----
| A |     | B |
-----     -----
  |         |
  |         |
  |         |
-----     -----
| C |     | D |
-----     -----
    \     /
     \   /
     -----
     | E |
     -----

MRO using super: [E, C, A, D, B, OBJECT, object]
MRO using superior: [E, C, A, OBJECT, object, D, B]

"""

from superior import superior, superiorMRO

class OBJECT(object):
    def __init__(self):
        print("OBJECT")

class A(OBJECT):
    def __init__(self):
        print("A")
        superior(A, self, "__init__")

class B(OBJECT):
    def __init__(self):
        print("B")
        superior(B, self, "__init__")

class C(A):
    def __init__(self, arg):
        print("C","arg=",arg)
        
        # Still works if we explicitly call __init__, instead of
        # superior(C, self, "__init__")
        A.__init__(self)

class D(B):
    def __init__(self, arg):
        print("D", "arg=",arg)
        superior(D, self, "__init__")

class E(C,D):
    def __init__(self, arg):
        print("E", "arg=",arg)
        superior(E, self, "__init__", arg)

if __name__ == "__main__":
    print("MRO (using super):", [x.__name__ for x in E.__mro__])
    print("MRO (using superior):", [x.__name__ for x in superiorMRO(E)])
    # TODO:
    #   Write a function that returns the superior MRO
    E(10)