from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    # string representation of object attributes
    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title, self.author, len(self.posts),
                                             's' if len(self.posts) != 1 else '')

    def create_post(self, post_title, post_content):
        self.posts.append(Post(post_title, post_content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }
