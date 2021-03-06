# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle (Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

    def __str__(self):
        return "Triangle with base" + str(self.base) + "and height" + str(self.height)

    def __eq__(self,other):
        return type(other) == Triangle and self.base == other.base and self.height == other.height

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.shape_arr = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if sh not in self.shape_arr:
            self.shape_arr.append(sh)
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        return iter(self.shape_arr)
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        for shape in self.shape_arr:
            if type(shape) == Circle:
                print ("Circle with radius " + str(shape.radius) )
            if type(shape) == Square:
                print ("Square with side " + str(shape.side) )
            if type(shape) == Triangle:
                print ("Triangle with base " + str(shape.base) + " and height " + str(shape.height) )

#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    largest_arr = []
    for sh in shapes:
        if sh.area() == max( [i.area() for i in shapes] ):
            largest_arr.append(sh)
    print(largest_arr.__str__())
    return tuple(largest_arr)




#
# Problem 4: Read shapes from a file into a ShapeSet
#
# def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found. 
    filename: string
    """
    ## TO DO

tg1 = Triangle(3,4)
tg2 = Triangle(4,5)
tg3 = Triangle(4,3)
v1= Square(1)
v2= Square(2)
t1= Circle(1)
t2= Circle(12)

ss = ShapeSet()

ss.addShape(tg1)
ss.addShape(v2)
ss.addShape(t2)
ss.addShape(tg3)

largest = findLargest(ss)
for e in largest:
    print (e)
print(largest[0] is t2)
# print(largest)
# print(ss.__str__())
