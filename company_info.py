from typing import List

class Review:
    def __init__(self, author: str, content: str):
        self.author = author
        self.content = content

class CompanyInfo:
    def __init__(self, name: str = "Hacktivate Nation", description: str = "Your trusted AI partner.", reviews: List[Review] = []):
        self.name = name
        self.description = description
        self.reviews = reviews

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'reviews': [review.__dict__ for review in self.reviews]
        }
