class ContactForm:
    def __init__(self, name=None, email=None, subject=None, message=None):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def validate(self):
        # Simple validation to check if all fields are filled
        return all([self.name, self.email, self.subject, self.message])

