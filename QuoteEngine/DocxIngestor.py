"""Docx Importer."""
from typing import List
from docx import Document

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class responsible on .docx imports."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Browse docx file and return a list of Quote objects."""
        if not cls.can_ingest(path):
            raise Exception('can not ingest file extension exception')

        quotes = []
        doc = Document(path)

        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                splits = paragraph.text.split('-')
                new_quote = QuoteModel(splits[0], splits[1])
                quotes.append(new_quote)

        return quotes
