import re
from django.core.exceptions import ValidationError

class Isbn:
    def __init__(self, isbn: str):
        self.isbn = isbn
        self.parts = self.parse_isbn(isbn)

        if not self.is_valid_isbn():
            raise ValidationError(f"{isbn} n'est pas un ISBN valide.")

    def parse_isbn(self, isbn: str):
        """
        Parse et divise un ISBN en ses parties (préfixe, groupe, éditeur, publication, contrôle).
        """
        pattern = r'^(97[89])-([0-9]+)-([0-9]+)-([0-9]+)-([0-9X])$'
        match = re.match(pattern, isbn)
        if not match:
            raise ValidationError(f"{isbn} n'est pas au format ISBN valide.")
        return {
            "prefix": match.group(1),
            "group": match.group(2),
            "publisher": match.group(3),
            "title": match.group(4),
            "check_digit": match.group(5)
        }

    def is_valid_isbn(self):
        """
        Valide le code de contrôle pour l'ISBN-13.
        """
        digits = [int(x) if x.isdigit() else 10 for x in self.isbn.replace("-", "")[:-1]]
        check_digit = self.isbn[-1]
        check_digit = 10 if check_digit == 'X' else int(check_digit)
        calculated = 10 - sum(d if i % 2 == 0 else d * 3 for i, d in enumerate(digits)) % 10
        return calculated == check_digit

    def __str__(self):
        """
        Retourne l'ISBN en tant que chaîne formatée.
        """
        return f"{self.parts['prefix']}-{self.parts['group']}-{self.parts['publisher']}-{self.parts['title']}-{self.parts['check_digit']}"

    def to_int(self):
        """
        Convertit l'ISBN en un entier.
        """
        return int(self.isbn.replace("-", "").replace("X", "10"))
