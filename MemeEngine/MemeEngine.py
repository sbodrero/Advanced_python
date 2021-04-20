"""Meme generator."""
import random
import os
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Meme generator class."""

    def __init__(self, output_dir):
        """Meme constructor."""
        self.output_dir = output_dir

    @staticmethod
    def resize_image(image, width):
        """Resize image with to with arg if needed."""
        if image.size[0] > width:
            return image
        ratio = width / float(image.size[0])
        height = int(ratio * float(image.size[1]))
        image = image.resize((width, height), Image.NEAREST)
        return image

    @staticmethod
    def draw_text(image, text, author,):
        """Add quote to image."""
        if text is None:
            raise Exception('Text Required')

        else:
            message = f"{text} {author}"
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('./font/LilitaOne-Regular.ttf', size=20)
            position = (
                random.choice(range(0, 100)),
                random.choice(range(0, 100))
            )
            draw.text(position, message, font=font, fill='white')
            del draw

    def make_meme(self, img_path, text, author, width=500):
        """Load, resize, add quote and save an image."""
        image = None
        output_path = None

        try:
            image = Image.open(img_path)
        except OSError as err:
            print("Could not open image OS error: {0}".format(err))

        if image:
            image = self.resize_image(image, width)
            self.draw_text(image, text, author)
            file_name, file_extension = os.path.splitext(img_path)
            file_name = file_name.split('/')
            output_path = f'{self.output_dir}/{file_name[-1]}{file_extension}'
            image.save(output_path)

        return output_path
