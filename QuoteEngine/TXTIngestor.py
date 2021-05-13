"""Module to ingest txt file types."""
from .IngestorInterface import IngestorInterface

from typing import List
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Ingestor to extract quotes from txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file and return a list of Quote Model objects.
        A '-' is required to separate the quote and author.

        Keyword arguments:
            path (str) -- file path to file that contains various quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')

        quotes = []

        try:
            f = open(path, 'r')

        except FileNotFoundError:
            raise Exception('Invalid file path. Please enter a valid path.')

        for line in f.readlines():
            line = line.strip()
            if '-' not in line:
                continue
            parse = line.split('-')
            parse = list(map(lambda x: x.strip('\ufeff')
                             .strip().strip('"'), parse))
            quote = QuoteModel(parse[0], parse[1])
            quotes.append(quote)
        f.close()
        return quotes
