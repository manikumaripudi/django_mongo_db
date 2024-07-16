from mongoengine import Document, fields

class django_data(Document):
    name = fields.StringField(required=True, max_length=100)
    description = fields.StringField()

    def __str__(self):
        return self.name
