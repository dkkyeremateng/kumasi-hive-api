from werkzeug.security import check_password_hash, generate_password_hash

from website.extensions import db


class Student(db.Document):
    """
    This is the Student model
    """
    external_id = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    is_active = db.BooleanField(required=True, default=True)
    display_pic = db.StringField(required=True)
    interests = db.ListField(required=True)
    courses = db.ListField()
    gender = db.StringField(required=True)
    telephone = db.StringField(required=True)

    meta = {'collection': 'students'}

    @classmethod
    def find_by_status(cls, status=True):
        """
        Find a user by their e-mail or username.

        :param status: is_live
        :type status: str
        :return: User instance
        """
        return Student.objects.filter(is_active=status)

    @classmethod
    def find_by_external_id(cls, external_id, is_active=True):
        """
        Find a user by their e-mail or username.

        :param external_id: external_id
        :type external_id: str
        :param is_active: is_active
        :type is_active: bool
        :return: User instance
        """
        return Student.objects.filter(external_id=external_id, is_active=is_active).first()

    @classmethod
    def encrypt_password(cls, plaintext_password):
        """
        Hash a plaintext string using PBKDF2. This is good enough according
        to the NIST (National Institute of Standards and Technology).

        In other words while bcrypt might be superior in practice, if you use
        PBKDF2 properly (which we are), then your passwords are safe.

        :param plaintext_password: Password in plain text
        :type plaintext_password: str
        :return: str
        """
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    def authenticated(self, with_password=True, password=''):
        """
        Ensure a user is authenticated, and optionally check their password.

        :param with_password: Optionally check their password
        :type with_password: bool
        :param password: Optionally verify this as their password
        :type password: str
        :return: bool
        """
        if with_password:
            return check_password_hash(self.password, password)

        return True
