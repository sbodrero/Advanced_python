"""CSV Importer."""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class responsible on .csv imports."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Browse csv file and return a list of Quote objects."""
        if not cls.can_ingest(path):
            raise Exception('can not ingest file extension exception')

        quotes = []

        dataframe = pandas.read_csv(path, header=0)

        for index, row in dataframe.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
