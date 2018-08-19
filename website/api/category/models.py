from datetime import datetime

from website.extensions import db


class Category(db.Document):
    """
    This is Course Document
    """
    category_name = db.StringField(required=True)
    date_created = db.DateTimeField(default=datetime.utcnow())
    is_live = db.BooleanField(default=True)

    @classmethod
    def find_by_status(cls, status=True):
        return cls.objects.filter(is_live=status)
