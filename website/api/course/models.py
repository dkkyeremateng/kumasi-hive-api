from datetime import datetime

from website.extensions import db
# from website.api.category.models import Category


class Course(db.Document):
    """
    This is Course Document
    """

    title = db.StringField(required=True, unique=True)
    external_id = db.StringField(required=True)
    description = db.StringField(required=True)
    is_completed = db.BooleanField(default=False)
    is_live = db.BooleanField(default=True)
    ending_date = db.DateTimeField(required=True)
    date_created = db.DateTimeField(default=datetime.utcnow())
    duration = db.StringField(required=True)
    # category = db.ReferenceField(Category)
    starting_date = db.DateTimeField(required=False)
    display_picture = db.URLField(required=True)
    user_id = db.StringField(required=True)
    what_you_will_learn = db.ListField(required=True)
    requirements = db.ListField(required=True)
    curriculum = db.DictField(required=True)
    target_audience = db.ListField(required=True)

    meta = {'collection': 'courses'}

    @classmethod
    def find_by_status(cls, is_completed=False):
        return cls.objects.filter(is_completed=is_completed, is_live=True)

    @classmethod
    def find_by_id(cls, course_id):
        return cls.objects.filter(external_id=course_id,
                                  is_live=True).first()
