"""Meme Generator Application."""
import random
import os
import requests
from flask import Flask, render_template, request

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeGenerator

from PIL import Image
from io import BytesIO

app = Flask(__name__)
meme = MemeGenerator('static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "_data/photos/dog/"

    # images within the images images_path directory
    images_path = "_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    file_type = image_url.split('.')[-1]
    accepted_file_types = ['jpg', 'png']
    if file_type not in accepted_file_types:
        raise Exception(f'Image file type must be {accepted_file_types}')

    r = requests.get(image_url)
    i = Image.open(BytesIO(r.content))
    tmp_file = f'./tmp_image_{random.randint(0, 100000000)}.{file_type}'
    i.save(tmp_file)

    body = request.form['body']
    author = request.form['author']
    quote = QuoteModel(body, author)
    path = meme.make_meme(tmp_file, quote.body, quote.author)

    os.remove(tmp_file)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
