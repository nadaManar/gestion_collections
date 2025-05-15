from django.db import models
from django.forms import ValidationError

from .validators import Isbn

class IsbnField(models.CharField):
    description = "Un champ personnalisé pour stocker un ISBN."

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 17  # Format max : "978-123-456-789-0"
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        """
        Convertit la valeur brute en un objet Isbn.
        """
        if not value:
            return None
        if isinstance(value, Isbn):
            return value
        return Isbn(value)

    def validate(self, value, model_instance):
        """
        Valide la valeur du champ.
        """
        super().validate(value, model_instance)
        if value and not value.is_valid_isbn():
            raise ValidationError(f"{value} n'est pas un ISBN valide.")
