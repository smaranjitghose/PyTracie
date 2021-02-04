from math import sqrt


class Sphere:
    """
    A 3D shape with centre, radius and material
    """

    def __init__(self, center, radius, material):
        """
        Dunder method to create the constructor for Sphere class
        """
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """
        Function to check if a ray intersects the spehre.
        Returns distance of intersection or None if there is no intersection
        """
        sphere_to_ray = ray.origin - self.center
        a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist

        return None
