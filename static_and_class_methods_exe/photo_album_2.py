from math import ceil


class PhotoAlbum:
    _page_capacity = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.__photo_builder()

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count/PhotoAlbum._page_capacity)
        return cls(pages)

    def add_photo(self, label: str):
        for r_index, row in enumerate(self.photos):
            if len(row) < PhotoAlbum._page_capacity:
                self.photos[r_index].append(label)
                return f"{label} photo added successfully on page {r_index + 1} slot {len(self.photos[r_index])}"
        return "No more free slots"

    def display(self):
        result = "-----------" + "\n"
        for row in self.photos:
            result += " ".join("[]" for _ in row) + "\n"
            result += "-----------" + "\n"
        return result.strip()

    def __photo_builder(self):
        result = []
        for _ in range(self.pages):
            result.append([])
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