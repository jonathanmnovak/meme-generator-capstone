"""Module to ingest Docx file types."""
from .IngestorInterface import IngestorInterface

from typing import List
from .QuoteModel import QuoteModel
import docx
import re


class DocxIngestor(IngestorInterface):
    """Ingestor to extract quotes from Docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file and return a list of Quote Model objects.

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
        else:
            f.close()

        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                parse = list(map(lambda x: x.strip('" '), parse))
                parse = list(map(lambda x: re.sub("\u2019", "'", x), parse))
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        return quotes
