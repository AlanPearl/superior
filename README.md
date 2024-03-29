# superior
A proposed inheritance tool to replace Python's super. This micro-project was motivated by and all current tests come from fuhm.net/super-harmful/

# Bugs
-Due to the way superior is implemented (very naively), it may not work if superior is called twice on two different inherited methods. It uses a set to keep track of the parent classes which have already been called for a given object, but doesn't actually track which methods have been called in the parent classes. The example below would fail if you had used super in place of superior:

```
from superior import superior

class Quadrilateral:
    def set_number_of_vertices(self):
        print("Setting number of vertices...")
        self.number_of_verts = 4
    
    def set_sum_of_angles(self):
        print("Setting sum of angles...")
        self.sum_of_angles = 360.0

class Square(Quadrilateral):
    def set_angle(self):
        print("Setting value of single angle...")
        
        superior(Square, self, "set_sum_of_angles")
        superior(Square, self, "set_number_of_vertices") # ignored wrongly
        
        self.angle = self.sum_of_angles / self.number_of_verts

class MrSquare(Square):
    def __init__(self):
        print("Mr. Square is thinking...")
        
        superior(MrSquare, self, "set_angle")
        superior(MrSquare, self, "set_number_of_verts") # ignored correctly
        superior(MrSquare, self, "set_sum_of_angles") # ignored correctly
        
        print("Mr. Square has", self.number_of_verts,
              "vertices, each with an angle of", self.angle,
              "which sums to", self.sum_of_angles, "in total.")

MrSquare()
```
