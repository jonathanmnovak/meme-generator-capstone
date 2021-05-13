"""Module that generates a meme."""
from PIL import Image, ImageDraw, ImageFont
from QuoteEngine import QuoteModel
from random import randint
import os
import warnings


class MemeGenerator:
    """Meme generator that loads a file, transforms it, and adds a caption."""

    def __init__(self, output_dir: str):
        """Create object and output the image to the output directory.

        Keyword Arguments:
            output_dir (str) -- Directory where to output the generated meme.
        """
        if not os.path.isdir(output_dir):
            warnings.warn(f'{output_dir} not found. Creating directory...')
            os.mkdir(output_dir)

        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str, author: str,
                  width=500) -> str:
        """Return a meme which is resized and contains a caption.

        Keyword Arguments:
            img_path (str) -- The file path to the image
            text (str) -- The quote body.
            author (str) -- The author of the quote.
            width (int) -- The width of the new image which is less than 500px.
        """
        try:
            f = open(img_path, 'r')
        except IOError:
            raise Exception('Invalid file path. Please enter a valid path.')
        else:
            f.close()

        im = Image.open(img_path)
        height = im.size[1]

        # Resize image
        assert width <= 500, f'Width must be less than 500px'
        ratio = width / float(im.size[0])
        height = int(ratio * float(height))
        meme_img = im.resize((width, height), Image.NEAREST)

        # Create font
        total_pixels = height*width
        font_size = int(total_pixels*0.0001)
        if font_size <= 10:
            font_size = 10
        fnt = ImageFont.truetype("./Fonts/arial.ttf", font_size)

        # Add quote and author to image
        draw = ImageDraw.Draw(meme_img)
        quote = QuoteModel(text, author)

        # Randomly choosing coordinates to place the text that is dynamic
        rand_width = randint(0, width)
        rand_height = randint(0, height)

        width_anchor = 'l'
        height_anchor = 't'

        if rand_width >= width*.75:
            width_anchor = 'r'
        elif rand_width >= width*.25:
            width_anchor = 'm'
        if rand_height >= height*.75:
            height_anchor = 'b'
        elif rand_height >= height*.25:
            height_anchor = 'm'

        anchor = width_anchor + height_anchor

        draw.text((rand_width, rand_height), str(quote), anchor=anchor,
                  font=fnt)

        # Output meme image
        output_filename = 'meme_' + img_path.split('/')[-1]
        output_path = self.output_dir + '/' + output_filename
        meme_img.save(output_path)
        return output_path
