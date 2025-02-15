import math

class Vector:
    """
    A three dimensional vector for usage in 3D computer graphics
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        Dunder method to declare the constructor method for our Vector class
        """
        self.x = x
        self.y = y
        self.z = z

    
    def __str__(self):
        """
        Dunder Method to represent the objects as strings for meaningful output formatting in a human readable form
        """
        return f"Vector object with coordinates x = {self.x}, y = {self.y} and z = {self.z}"

    def __repr__(self):
        """
        Dunder Method to represent the objects as strings for meaningful output formatting 
        """
        return f"Vector(x = {self.x}, y = {self.y}, z = {self.z})"

    def __eq__(self,other):
        """
        Dunder method to check equality of two vectors
        This is a life saver while using unittest to assertEqual two objects
        """
        return self.x == other.x and self.y == other.y and self.z == other.z 

      
    ## For now custom matcher object is avoided for unit testing

    def dot_product(self, other):
        """
        Method to  compute the dot product of two vectors
        """
        return self.x*other.x + self.y*other.y + self.z*other.z
      
    def magnitude(self):
        """
        Method to  compute the magnitude of a vector.
        Magnitude of a vector can also be defined as the square root of the dot product of a vector with itself.
        """
        return math.sqrt(self.dot_product(self))
      
    def normalize(self):
        """
        Method to compute the normalized vector i.e. the vector divided by its magnitude
        """
        return self/self.magnitude()
      
    def __add__(self,other):
        """
        Dunder method to overload the addition operator
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)  
      
    def __sub__(self,other):
        """
        Dunder method to overload the subtraction operator
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z) 
      
    def __mul__(self,other):
        """
        Dunder method to overload the mutliplication operator
        """
        assert not isinstance(other,Vector) # To ensure that our mutliplication only works for scalar multiplication
        return Vector(self.x* other, self.y*other, self.z*other) 
      
    def __rmul__(self,other):
        """
        Dunder method to overload the mutliplication operator but with the reverse order of operands (since our multiplication is commutative)
        """
        return self.__mul__(other,self) 

    def __truediv__(self,other):
        """
        Dunder method to overload the division operator
        """ 
        assert not isinstance(other, Vector) # To ensure that our division only works for scalar division
        return Vector(self.x/other, self.y/other, self.z/other)
