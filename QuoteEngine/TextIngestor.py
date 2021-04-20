"""TXT Importer."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Class responsible on .txt imports."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Browse txt file and return a list of Quote objects."""
        if not cls.can_ingest(path):
            raise Exception('can not ingest file extension exception')

        quotes = []

        with open(path, 'r') as txt_file:
            for line in txt_file:
                if line != "":
                    splits = line.split('-')
                    new_quote = QuoteModel(splits[0], splits[1])
                    quotes.append(new_quote)

        return quotes
