"""Importer interface."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class fro importers."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check if importer can read file."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Browse file and return a list of Quote objects."""
        pass
