class Person(object):
    """Person Class.

    Attributes:
        person_name: Full name of the person.
    """

    def __init__(self, person_name):
        self.person_name = person_name

class Fellow(Person):
    """ Fellow Class. Inherits from Person class.

    Attributes:
        person_job_type: Is Fellow.
    """

    def __init__(self, person_name):
        super(Fellow, self).__init__(person_name)
        self.person_job_type = "FELLOW"

class Staff(Person):
    """ Staff Class. Inherits from Person class.

    Attributes:
        person_job_type: Is Staff.
    """

    def __init__(self, person_name):
        super(Staff, self).__init__(person_name)
        self.person_job_type = "STAFF"

    