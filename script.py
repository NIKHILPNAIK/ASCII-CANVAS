import PIL.Image

# ASCII characters used to represent the pixels in the image (more characters for detail)
ASCII_CHARS = ["@", "#", "8", "&", "o", ":", "*", "+", ";", "=", "-", "_", ":", ",", ".", " "]

# Resize the image for the new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)  # Keep aspect ratio intact
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert image to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert the pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 16] for pixel in pixels])  # Change the divisor for finer detail
    return characters

def main(new_width=100):
    # Attempt to enter the path of the image
    path = input("Enter the path of the image: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(f"{path} is an Invalid path")
        return

    # Resize the image, convert to grayscale, then convert pixels to ASCII
    resized_image = resize_image(image, new_width)
    grayscale_image = grayify(resized_image)
    new_image_data = pixels_to_ascii(grayscale_image)

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    # Save the image to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

# Call the main function
main(new_width=100)
