"""Module to define the quote data model."""


class QuoteModel:
    """Quote model for the meme generator."""

    def __init__(self, body: str, author: str):
        """Quote model object.

        Keyword arguments:
            body (str) -- body of a specific quote.
            author (str) -- author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return the string representation for the QuoteModel object."""
        return f'"{self.body}" - {self.author}'
