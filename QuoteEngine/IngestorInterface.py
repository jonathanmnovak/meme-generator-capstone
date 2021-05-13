"""Module to setup the ingestor interface."""
from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface to extract quotes from different file formats."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether the file type can be ingested or not.

        Keyword arguments:
            path (str) -- file path to file that contains various quotes.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file and create Quote Model objects.

        Keyword arguments:
            path (str) -- file path to file that contains various quotes.
        """
        pass
