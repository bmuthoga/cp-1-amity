class Person(object):
    """Person Class.

    Attributes:
        person_name: Full name of the person.
        person_wants_accomodation: Whether the person wants accomodation or not.
    """

    def __init__(self, person_name, person_wants_accomodation):
        self.person_name = person_name
        self.person_wants_accomodation = person_wants_accomodation

class Fellow(Person):
    """ Fellow Class. Inherits from Person class.

    Attributes:
        person_job_type: Is Fellow.
    """

    def __init__(self, person_job_type):
        self.person_job_type = "Fellow"

class Staff(Person):
    """ Staff Class. Inherits from Person class.

    Attributes:
        person_job_type: Is Staff.
    """

    def __init__(self, person_job_type):
        self.person_job_type = "Staff"

    