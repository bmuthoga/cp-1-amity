class Room(object):
    """Room Class.

    Attributes:
    room_name: The name of the room.
    room_vacancy: The vacancy of the room.
    room_occupants: The occupants of the room.
    """

    def __init__(self, room_name, room_vacancy, room_occupants):
        self.room_name = room_name
        self.room_vacancy = room_vacancy
        self.room_occupants = room_occupants

class LivingSpace(Room):
    """LivingSpace Class.

    Attributes:
    room_type: The type of the room. Is a living space.
    room_capacity: The capacity the room can hold.
    """

    def __init__(self, room_type, room_capacity):
        self.room_type = "Living space"
        self.room_capacity = 4

class Office(Room):
    """Office Class.

    Attributes:
    room_type: The type of the room. Is an office.
    room_capacity: The capacity the room can hold.
    """

    def __init__(self, room_type, room_capacity):
        self.room_type = "Office"
        self.room_capacity = 6