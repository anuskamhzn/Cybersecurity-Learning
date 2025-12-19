from PIL import Image

def decode_image(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_data = ""

    for pixel in pixels:
        for color in pixel:
            binary_data += str(color & 1)

            if binary_data.endswith("1111111111111110"):
                message = binary_data[:-16]
                text = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))
                print("Hidden Message:", text)
                return

    print("No hidden message found.")

if __name__ == "__main__":
    decode_image("output_image.png")
