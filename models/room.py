class Room(object):
    """Room Class.

    Attributes:
    room_name: The name of the room.
    """

    def __init__(self, room_name):
        self.room_name = room_name

class LivingSpace(Room):
    """LivingSpace Class. Inherits from Room class.

    Attributes:
    room_type: The type of the room. Is a livingspace.
    room_capacity: The capacity the room can hold. Is 4.
    """

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
        self.room_type = "LIVINGSPACE"
        self.room_capacity = 4

class Office(Room):
    """Office Class. Inherits from Room class.

    Attributes:
    room_type: The type of the room. Is an office.
    room_capacity: The capacity the room can hold. Is 6.
    """

    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.room_type = "OFFICE"
        self.room_capacity = 6
        