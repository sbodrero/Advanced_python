"""PDF Importer."""
import subprocess
import os
import random
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PdfIngestor(IngestorInterface):
    """Class responsible on .pdf imports."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Browse pdf file and return a list of Quote objects."""
        if not cls.can_ingest(path):
            raise Exception('can not ingest file extension exception')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'

        try:
            subprocess.call(['pdftotext', path, tmp])
        except OSError as e:
            print(f"Error with pdftotex librairy OS error: {0}")

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                splits = line.split('-')
                new_cat = QuoteModel(splits[0], splits[1])
                quotes.append(new_cat)

        file_ref.close()
        os.remove(tmp)
        return quotes
