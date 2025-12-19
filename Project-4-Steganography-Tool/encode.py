from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text) + '1111111111111110'

def encode_image(image_path, secret_text, output_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_text = text_to_binary(secret_text)
    data_index = 0
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel

        if data_index < len(binary_text):
            r = (r & ~1) | int(binary_text[data_index])
            data_index += 1
        if data_index < len(binary_text):
            g = (g & ~1) | int(binary_text[data_index])
            data_index += 1
        if data_index < len(binary_text):
            b = (b & ~1) | int(binary_text[data_index])
            data_index += 1

        new_pixels.append((r, g, b))

    image.putdata(new_pixels)
    image.save(output_path)
    print("Message hidden successfully.")

if __name__ == "__main__":
    image = input("Enter image name: ")
    message = input("Enter secret message: ")
    output = input("Enter output image name: ")

    encode_image(image, message, output)

