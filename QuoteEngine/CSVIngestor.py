"""Module to ingest CSV file types."""
from .IngestorInterface import IngestorInterface

from typing import List
from .QuoteModel import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):
    """Ingestor to extract quotes from CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file and return a list of Quote Model objects.
        File must have a body and author column headers.

        Keyword arguments:
            path (str) -- file path to file that contains various quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')

        quotes = []
        try:
            df = pd.read_csv(path, header=0)
        except FileNotFoundError:
            raise Exception('Invalid file path. Please enter a valid path.')

        required_cols = ['body', 'author']
        for col in required_cols:
            assert col in df.columns, \
                f"The {col} column header is missing from the file."

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
