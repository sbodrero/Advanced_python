"""Quote handler."""


class QuoteModel:
    """Build a Quote object."""

    def __init__(self, body, author):
        """Quote constructor."""
        self.body = body
        self.author = author
