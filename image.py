class Image():

    def __init__(self, width, height):
        """
        Dunder method to create a constructor for initializing the image
        """
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]
        
    def set_pixel(self, x, y, color):
        """
        Method to the color of the pixel at the intersection of xth row and yth column
        """
        self.pixels[x][y] = color 
    
    def write_ppm(self, img_file):
        """
        Function to save the image object in Portable Pixel Map file format
        """

        def rescale_color(c):
            """
            Nested function to rescale the color from 0-1 range to 0-255
            """
            # Should be a round number
            # Maximum value should not exceed 255
            # Minimum value should not be less than 0
            return round(max(min(c*255,255),0))
        
        img_file.write(f"P3 {self.width} {self.height}\n255\n")
        for row in self.pixels:
            for color in row:
                img_file.write(f"{rescale_color(color.x)} {rescale_color(color.y)} {rescale_color(color.z)} ")
            img_file.write("\n")

