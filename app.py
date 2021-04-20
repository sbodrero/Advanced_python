"""Server app execution."""
import os
import random
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
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
    body = request.form.get('body')
    author = request.form.get('author')
    image = request.form.get('image_url')
    path = None

    if image is not None:
        response = requests.get(image,  allow_redirects=True)
        tmp = f'./tmp/{random.randint(0, 1000000)}.png'
        file = open(tmp, 'wb')
        file.write(response.content)
        file.close()
        path = meme.make_meme(tmp, body, author)
        del tmp
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
