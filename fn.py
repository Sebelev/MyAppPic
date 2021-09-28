from PIL import Image



def load_image(image_file):
    img = Image.open(image_file)
    return img


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def image_pixel(image_file):
    image = load_image(image_file)
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()
    pix_list = list()
    for i in range(width):
        for j in range(height):
            pix_list.append(rgb_to_hex(pix[i, j]))

    return tuple(pix_list)
