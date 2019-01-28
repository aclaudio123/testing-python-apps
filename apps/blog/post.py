# A post class representing a single post that goes into blog
# A post has two properties, a title and content


class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # send post as json
    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }
