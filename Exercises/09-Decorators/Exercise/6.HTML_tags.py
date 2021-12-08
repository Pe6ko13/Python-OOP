def tags(tag_):
    def decor(func):
        def wrap(*args):
            res = func(*args)
            return f'<{tag_}>{res}</{tag_}>'
        return wrap
    return decor


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
