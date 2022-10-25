from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room_number == room.number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room_number == room.number:
                room.free_room()

    def _get_all_guests(self):
        guests = 0
        for room in self.rooms:
            guests += room.guests
        return guests

    def _get_all_free_rooms(self):
        free_rooms = ", ".join([str(x.number) for x in self.rooms if not x.is_taken])
        return free_rooms

    def _get_all_taken_rooms(self):
        taken_rooms = ", ".join([str(x.number) for x in self.rooms if x.is_taken])
        return taken_rooms

    def status(self):
        result = f"Hotel {self.name} has {self._get_all_guests()} total guests" + "\n"\
        + f"Free rooms: {self._get_all_free_rooms()}" + "\n"\
        + f"Taken rooms: {self._get_all_taken_rooms()}"
        return result
