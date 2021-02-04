from color import Color
from image import Image

# Classic wikipedia example


def main():
    # Declare the constants
    WIDTH = 3
    HEIGHT = 2
    # Create an image
    img = Image(WIDTH, HEIGHT)
    # Set Primary Colors
    red = Color(x=1, y=0, z=0)
    green = Color(x=0, y=1, z=0)
    blue = Color(x=0, y=0, z=1)
    # Set individual pixel values
    img.set_pixel(0, 0, red)
    img.set_pixel(0, 1, green)
    img.set_pixel(0, 2, blue)
    img.set_pixel(1, 0, red + green)
    img.set_pixel(1, 1, red + green + blue)
    img.set_pixel(1, 2, red * 0.001)
    # Save the image
    with open("demo.ppm", "w") as img_file:
        img.write_ppm(img_file)

    # To see an image of this proportion, prefer using matplotlib.pyplot.imshow
    # Read the image using cv2


if __name__ == "__main__":
    main()
