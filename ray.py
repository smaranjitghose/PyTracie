class Ray:
    """
    Ray is a mathematical quantity with an origin and a normalised direction
    """

    def __init__(self, origin, direction):
        """
        Dunder method to create constructor for Ray class
        """
        self.origin = origin
        self.direction = direction.normalize()
