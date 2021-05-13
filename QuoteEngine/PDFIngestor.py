"""Module to ingest pdf file types."""
from .IngestorInterface import IngestorInterface

from typing import List
from .QuoteModel import QuoteModel
from QuoteEngine import TXTIngestor
import subprocess
import os


class PDFIngestor(IngestorInterface):
    """Ingestor to extract quotes from pdf files."""

    allowed_extensions = ['pdf']
    # location of the pdftotext XpdfReader binary file
    pdftotext = './xpdf-tools-mac-4.03/bin64/pdftotext'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file and return a list of Quote Model objects.

        Keyword arguments:
            path (str) -- file path to file that contains various quotes.
        """
        tmp_txt = "./tmp_txt.txt"

        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type')

        if not os.path.isfile(cls.pdftotext):
            raise Exception(f'Xpd Reader not found at {cls.pdftotext}.'
                            f'Please update the pdftotext path in the '
                            f'PFD.Ingestor.py to the location of the binary '
                            f'file.')

        try:
            f = open(path, 'r')
        except IOError:
            raise Exception('Invalid file path. Please enter a valid path.')
        else:
            f.close()

        subprocess.run([cls.pdftotext, '-layout', path, tmp_txt])

        quotes = TXTIngestor.parse(tmp_txt)

        os.remove(tmp_txt)

        return quotes
