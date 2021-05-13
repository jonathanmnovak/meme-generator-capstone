"""File to generate memes."""
import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeGenerator


def generate_meme(path=None, body=None, author=None) -> str:
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        if author is not None:
            raise Exception('Body is required if an Author is given')
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author is required if Body is given')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Random Meme Generator!')
    parser.add_argument('--path', type=str, default=None,
                        help='File path to an image')
    parser.add_argument('--body', type=str, default=None,
                        help='Quote body to add to the image')
    parser.add_argument('--author', type=str, default=None,
                        help='Quote author to add to the image')
    args = parser.parse_args()
    if args.path is not None:
        try:
            f = open(args.path, 'r')
        except FileNotFoundError:
            raise Exception('Invalid file path. Please enter a valid path.')
        else:
            f.close()
    print(generate_meme(args.path, args.body, args.author))
