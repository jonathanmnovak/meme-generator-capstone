"""Ingestor class that realizes the IngestorInterface abstract base class."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Ingestor that encapsulates helper classes."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Check the file type, parse the file using the correct class,
        and return a list of Quote Model objects.

        Keyword arguments:
            path (str) -- file path to file that contains various quotes.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise Exception(f'File type {path.split(".")[-1]} not supported.')
