import os
import random
from models.person import Fellow, Staff
from models.room import LivingSpace, Office

class Amity(object):
    """ Amity Facility.

    Attributes:
        staff: A list containing Amity's staff.
        fellows: A list containing Amity's fellows.
        all_people: A list containing everyone at Amity.
        rooms: A list containing Amity's rooms.
        offices: A list containing Amity's offices.
        living_spaces: A list containing Amity's living spaces.
        office_allocations: A list containing persons allocated to offices.
        living_space_allocations: A list containing persons allocated to living spaces.
    """

    staff = []
    fellows = []
    all_people = []
    rooms = []
    offices = []
    living_spaces = []
    office_allocations = []
    living_space_allocations = []

    @classmethod
    def create_room(cls, room_name, room_type):
        """This method creates a new room for Amity."""

        room_name = room_name.upper()
        room_type = room_type.upper()
        if room_name in Amity.rooms:
            return "%s already exists." % (room_name)
        else:
            if room_type == "LIVING SPACE":
                Amity.rooms.append(room_name)
                Amity.living_spaces.append(room_name)
                return "%s created" % (room_name)
            elif room_type == "OFFICE":
                Amity.rooms.append(room_name)
                Amity.offices.append(room_name)
                return "%s created" % (room_name)
            else:
                raise ValueError("Invalid room type. Try again.")

    @classmethod
    def add_person(cls, person_name, person_wants_accomodation, person_job_type):
        """This method creates a new member of Amity.
            Allocates the member an office and/or living space.
        """

        if person_name.isalpha() is False:
            raise ValueError("Invalid name input. Try again.")
        else:
            person_name.upper()
            person_wants_accomodation.upper()
            person_job_type.upper()
            if person_job_type == "FELLOW":
                Amity.fellows.append(person_name)
                Amity.all_people.append(person_name)
                if person_wants_accomodation == "YES":
                    return "YES test message"
                    # Add functionality to assign office and living space later.
                    # Add functionality to print Fellow name created and rooms allocated to.
                elif person_wants_accomodation == "NO":
                    return "NO test message"
                    # Add functionality to assign office later.
                    # Add functionality to print Fellow name created and office allocated to.
            elif person_job_type == "STAFF":
                Amity.staff.append(person_name)
                Amity.all_people.append(person_name)
                # Add functionality to assign office later.
                # Add functionality to print Staff name created and office allocated to.
            else:
                raise ValueError("Invalid job type. Try again.")

    @classmethod
    def allocate_living_space(self, person_name):
        """This method allocates a fellow a random living space."""

        
