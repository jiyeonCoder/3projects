import hashlib


class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username

        m = hashlib.sha256()
        self.password = m.update(password.encode('utf-8'))

    def display(self):
        return f"Name:{self.name}, Username:{self.username}"


class Post():
    def __init__(self, username, title, content):
        self.author = username
        self.title = title
        self.content = content


members = []
posts = []
while True:
    name = input('Name: ')
    username = input('Username: ')
    password = input('Password: ')

    person = Member(name, username, password)

    members.append(person)

    member_answer = input('Continue(Y/N)?')
    if member_answer == 'N':
        for m in members:
            while True:
                print(m.display())
                title = input('Title: ')
                content = input('content: ')
                post = Post(m.username, title, content)
                posts.append(post)
                comment_answer = input(
                    'Do you want to leave more comment(Y/N)?')
                if comment_answer == 'N':
                    break
        break

for p in posts:
    if p.author == 'apple':
        print('certain(apple) user wrote: ', p.title)
    if "great" in p.content:
        print('certain(great) word contained: ', p.title)
