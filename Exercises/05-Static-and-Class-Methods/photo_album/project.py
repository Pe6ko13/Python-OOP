import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(pages=math.ceil(photos_count / 4))

    def add_photo(self, label):
        for idx, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = []
        for p in self.photos:
            result.append('-' * 11)
            result.append(('[] ' * len(p)).rstrip(' '))
        result.append('-' * 11)
        return '\n'.join(result) + '\n'
        #return '\n'.join(['-' * 11 + '\n' + ' '.join('[]' * len(p)) for p in self.photos])
