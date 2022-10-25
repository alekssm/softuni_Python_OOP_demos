class PhotoAlbum:
    _page_capacity = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count)

    def _album_creator(self):
        matrix = []
        for n in range(self.pages):
            row = []
            for m in range(self._page_capacity):
                slot = 0
                row.append(slot)
            matrix.append(row)
        self.photos = matrix

    def add_photo(self, label:str):
        if not self.photos:
            self._album_creator()
        for r in range(len(self.photos)):
            for c in range(self._page_capacity):
                if self.photos[r][c] == 0:
                    self.photos[r][c] = label
                    return f"{label} photo added successfully on page {r+1} slot {c+1}"
        return "No more free slots"

    def display(self):
        result = "-----------" + "\n"
        for r in range(len(self.photos)):
            if self.photos[r] == [0] * self._page_capacity:
                result += "\n" + "-----------" + "\n"
            else:
                for c in range(self._page_capacity):
                    if not self.photos[r][c] == 0:
                        result += "[]"
                result += "\n" + "-----------" + "\n"
        return result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())