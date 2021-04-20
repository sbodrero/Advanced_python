"""Handle Ingestor."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PdfIngestor import PdfIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Class responsible on hnadle correct Ingestor."""

    Ingestors = [DocxIngestor, CSVIngestor, PdfIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Browse and return Ingestor based on file."""
        if path is None:
            raise Exception('Empty path')
        else:
            for ingestor in cls.Ingestors:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
