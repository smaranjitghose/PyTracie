from vector import Vector

class Color(Vector):
    """
    Stores colors as RGB triplets.An ALias for Vector
    """
    @classmethod
    def from_hex(cls, hexcolor = "#000000"):
        x = int(hexcolor[1:3], 16)/255.0
        x = int(hexcolor[3:5], 16)/255.0
        x = int(hexcolor[5:7], 16)/255.0
        return cls(x, y, z)

