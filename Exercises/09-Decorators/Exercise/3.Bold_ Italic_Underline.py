def make_bold(func):
    def wrapper(*args):
        return f'<b>{func(*args)}</b>'
    return wrapper\

def make_italic(func):
    def rapper(*args):
        return f'<i>{func(*args)}</i>'
    return rapper

def make_underline(func):
    def wrap(*args):
        return f'<u>{func(*args)}</u>'
    return wrap


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"
print(greet_all("Peter", "George"))
