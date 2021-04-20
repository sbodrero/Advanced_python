# Image Quote Engine

This application generates quotes from cvs, docx, txt or pdf file on a given resized image.

## Setting up the application

```bash
pip install requirements.txt
```

## Usage

via command line or shell

```python
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Getting args to make image with message

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      a path to an image
  --body BODY      the body of the message
  --author AUTHOR  the author of the message
```

Via internal flask server

```python
python app.py
```

## Modules 

The app contain two main modules.

**QuoteEngine module** is responsible for creating a message with body and author.
The message can be done via command line or from a random list of quotes imported 
from various given files (vcs, text, pdf or docx)

**MemeEngine module** takes an image, resize it if needed, add a quote and save 
the modified image to a given output.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)