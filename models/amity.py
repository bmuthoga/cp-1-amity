import os
import sqlalchemy
import random

from termcolor import colored, cprint

from .person import Fellow, Staff
from .room import LivingSpace, Office


class Amity(object):
    """ Amity Facility.

    Attributes:
        staff: A list containing Amity's staff.
        fellows: A list containing Amity's fellows.
        all_people: A list containing everyone at Amity.
        all_rooms: A list containing Amity's rooms.
        offices: A list containing Amity's offices.
        living_spaces: A list containing Amity's living spaces.
        office_allocations: A dictionary containing persons allocated to offices.
        living_space_allocations: A dictionary containing fellows allocated to living spaces.
        unallocated_living_spaces: A list containing fellows who haven't been allocated to
        living spaces.
        unallocated_offices: A list containing people who haven't been allocated to offices.
        person_data: A dictionary containing person id, name, job type and accomodation option.
        room_data: A dictionary containing room name, room type and room capacity.
    """

    staff = []
    fellows = []
    all_people = []
    all_rooms = []
    offices = []
    living_spaces = []
    office_allocations = {}
    living_space_allocations = {}
    unallocated_living_spaces = []
    unallocated_offices = []
    person_data = {}
    room_data = {}

    def create_room(self, room_name, room_type):
        """This method creates a new room for Amity."""

        room_name = room_name.upper()
        room_type = room_type.upper()

        if room_name in self.all_rooms:
            return "{} already exists." .format(room_name)

        else:
            if room_type == "LIVINGSPACE":
                new_room = LivingSpace(room_name)
                self.all_rooms.append(room_name)
                self.living_spaces.append(room_name)
                self.room_data[room_name] = [new_room.room_type, new_room.room_capacity]
                self.living_space_allocations[room_name] = []
                return "{} created" .format(room_name)

            elif room_type == "OFFICE":
                new_room = Office(room_name)
                self.all_rooms.append(room_name)
                self.offices.append(room_name)
                self.room_data[room_name] = [new_room.room_type, new_room.room_capacity]
                self.office_allocations[room_name] = []
                return "{} created" .format(room_name)

            else:
                return "Invalid room type. Try again."

    def add_person(self, person_name, person_job_type, person_wants_accomodation):
        """This method creates a new member of Amity and allocates the member an
            office and/or living space.
        """

        if person_name.isalpha() is False:
            return "Invalid person name. Try again."

        else:

            if person_job_type.upper() == "FELLOW":
                new_person = Fellow(person_name.upper())
                person_id = "F" + str(len(self.fellows) + 1)
                self.fellows.append(person_name.upper())
                self.all_people.append(person_name.upper())

                if person_wants_accomodation.upper() == "YES" or \
                    person_wants_accomodation.upper() == "Y":
                    self.person_data[person_id] = [new_person.person_name, \
                        new_person.person_job_type.upper(), \
                        person_wants_accomodation.upper()]
                    allocated_living_space = self.allocate_living_space(person_name.upper())
                    allocated_office = self.allocate_office(person_name.upper())
                    return "{} successfully added! \nAllocated to:\nLiving Space: {}\nOffice: {}" \
                            .format(person_name.upper(), allocated_living_space, allocated_office)

                elif person_wants_accomodation.upper() == "NO" or \
                    person_wants_accomodation.upper() == "N":
                    self.person_data[person_id] = [new_person.person_name, \
                        new_person.person_job_type.upper(), \
                        person_wants_accomodation.upper()]
                    allocated_office = self.allocate_office(person_name.upper())
                    return "{} successfully added! \nAllocated to:\nOffice: {}" \
                                .format(person_name.upper(), allocated_office)

                else:
                    return "Invalid accomodation input. Try again."

            elif person_job_type.upper() == "STAFF":
                new_person = Staff(person_name.upper())
                person_id = "S" + str(len(self.staff) + 1)
                self.staff.append(person_name.upper())
                self.all_people.append(person_name.upper())

                if person_wants_accomodation.upper() == "YES" or \
                    person_wants_accomodation.upper() == "Y":
                    return "No accomodation provided for Staff. Try again."

                elif person_wants_accomodation.upper() == "NO" or \
                    person_wants_accomodation.upper() == "N":
                    self.person_data[person_id] = [new_person.person_name, \
                        new_person.person_job_type.upper(), \
                        person_wants_accomodation.upper()]
                    allocated_office = self.allocate_office(person_name.upper())
                    return "{} successfully added! \nAllocated to:\nOffice: {}" \
                                .format(person_name.upper(), allocated_office)

                else:
                    return "Invalid accomodation input. Try again."

            else:
                return "Invalid job type. Try again."

    def allocate_living_space(self, fellow_name):
        """This method allocates a living space to a fellow."""

        vacant_living_spaces = []

        for room in self.living_spaces:

            if len(self.living_space_allocations[room]) < self.room_data[room][1]:
                vacant_living_spaces.append(room)

        if fellow_name not in self.all_people:
            return "{} does not exist." .format(fellow_name.upper())

        else:

            if vacant_living_spaces:

                for room in self.living_space_allocations:
                    if fellow_name.upper() in self.living_space_allocations[room]:
                        return "{} already allocated to a living space." \
                            .format(fellow_name.upper())

                random_living_space = random.choice(vacant_living_spaces)

                self.living_space_allocations[random_living_space].append(fellow_name.upper())

                if fellow_name in self.unallocated_living_spaces:
                    self.unallocated_living_spaces.remove(fellow_name)

                return "{} allocated to {}" .format(fellow_name.upper(), random_living_space)

            else:
                self.unallocated_living_spaces.append(fellow_name.upper())
                return "No vacant living spaces at the moment."

    def allocate_office(self, person_name):
        """This method allocates an office to a person."""

        vacant_offices = []

        for room in self.offices:

            if len(self.office_allocations[room]) < self.room_data[room][1]:
                vacant_offices.append(room)

        if person_name not in self.all_people:
            return "{} does not exist." .format(person_name.upper())

        else:

            if vacant_offices:

                for room in self.office_allocations:
                    if person_name.upper() in self.office_allocations[room]:
                        return "{} already allocated to an office." .format(person_name.upper())

                random_office = random.choice(vacant_offices)

                self.office_allocations[random_office].append(person_name.upper())

                if person_name in self.unallocated_offices:
                    self.unallocated_offices.remove(person_name)

                return "{} allocated to {}" .format(person_name.upper(), random_office)

            else:
                self.unallocated_offices.append(person_name.upper())
                return "No vacant offices at the moment."

    def reallocate_person(self, person_id, room_name):
        """This method reallocates a person to another specified room."""

        person_data_list = self.person_data.get(person_id.upper())
        room_data_list = self.room_data.get(room_name.upper())

        if person_data_list is None:
            return "{} does not exist. Try again." .format(person_id)

        elif room_data_list is None:
            return "{} does not exist. Try again." .format(room_name)

        else:
            person_name = person_data_list[0].upper()
            person_job_type = person_data_list[1]
            room_capacity = room_data_list[1]
            room_type = room_data_list[0]

            if room_type == "LIVINGSPACE":
                current_number_of_room_occupants = len(self.living_space_allocations[room_name])

                if person_name in self.living_space_allocations[room_name]:
                    return "{} already allocated to {}." .format(person_name, room_name)

                elif current_number_of_room_occupants == room_capacity:
                    return "{} already full." .format(room_name)

                elif person_job_type == "STAFF":
                    return "Cannot allocate a member of Staff to a living space."

                else:
                    for room in self.living_space_allocations:
                        for person in self.living_space_allocations[room]:
                            if person == person_name:
                                self.living_space_allocations[room].remove(person_name)
                                self.living_space_allocations[room_name].append(person_name)
                                return "{} has been successfully reallocated to {}." \
                                    .format(person_name, room_name.upper())

                    return "{} not yet allocated to any living space." .format(person_name)

            if room_type == "OFFICE":
                current_number_of_room_occupants = len(self.office_allocations[room_name.upper()])

                if person_name in self.office_allocations[room_name.upper()]:
                    return "{} already allocated to {}" .format(person_name, room_name)

                elif current_number_of_room_occupants == room_capacity:
                    return "{} already full." .format(room_name)

                else:
                    for room in self.office_allocations:
                        for person in self.office_allocations[room]:
                            if person == person_name:
                                self.office_allocations[room].remove(person_name)
                                self.office_allocations[room_name.upper()].append(person_name)
                                return "{} has been successfully reallocated to {}." \
                                    .format(person_name, room_name.upper())

                    return "{} not yet allocated to any office." .format(person_name)

    def load_people(self, filename):
        """This method adds people to rooms from a txt file."""

        if filename:
            people_file = open("models/" + filename + ".txt")
            people = people_file.readlines()
            people = (content.strip() for content in people)

            for person in people:
                person_data = person.split()
                person_name = person_data[0] + person_data[1]
                person_job_type = person_data[2]

                if person_job_type == "STAFF":
                    person_wants_accomodation = "NO"
                    self.add_person(person_name, person_job_type, person_wants_accomodation)

                elif person_job_type == "FELLOW":

                    if len(person_data) <= 3:
                        person_wants_accomodation = "NO"
                        self.add_person(person_name, person_job_type, person_wants_accomodation)

                    elif len(person_data) == 4:
                        accomodation_option = person_data[3]

                        if accomodation_option == "Y":
                            person_wants_accomodation = "YES"
                            self.add_person(person_name, person_job_type, person_wants_accomodation)

                        elif accomodation_option == "N":
                            person_wants_accomodation = "NO"
                            self.add_person(person_name, person_job_type, person_wants_accomodation)

                        elif accomodation_option != "Y" or accomodation_option != "N":
                            return "Invalid accomodaton input. Try again."

                    else:
                        return "Invalid number of arguments input. Try again."

                else:
                    return "Invalid job type. Try again."
            return "People successfully loaded."

        else:

            return "Filename must be provided. Try again."

    def print_allocations(self, filename):
        """This method prints a list of allocations onto the screen.
            Can also print them to a txt file if an optional -o option is specified.
        """

        if filename:
            file = open("models/" + filename + ".txt", "w")
            file.write("LIVING SPACE ALLOCATIONS\n")

            for room_name in self.living_space_allocations:
                file.write("\n{}\n" .format(room_name))
                file.write("-" * 20)
                file.write("\n")
                living_space_occupants = self.living_space_allocations[room_name]
                file.write(", ".join(living_space_occupants))
                file.write("\n")

            file.write("\n\nOFFICE ALLOCATIONS\n")

            for room_name in self.office_allocations:
                file.write("\n{}\n" .format(room_name))
                file.write("-" * 20)
                file.write("\n")
                office_occupants = self.office_allocations[room_name]
                file.write(", ".join(office_occupants))
                file.write("\n")

            return "Done."
        else:
            cprint("\nLIVING SPACE ALLOCATIONS", "blue")

            for room_name in self.living_space_allocations:
                living_space_occupants = self.living_space_allocations[room_name]
                cprint("\n{}" .format(room_name), "cyan")
                cprint("-" * 20, "cyan")
                cprint(", ".join(living_space_occupants), "green")

            cprint("\n\nOFFICE ALLOCATIONS", "blue")

            for room_name in self.office_allocations:
                office_occupants = self.office_allocations[room_name]
                cprint("\n{}" .format(room_name), "cyan")
                cprint("-" * 20, "cyan")
                cprint(", ".join(office_occupants), "green")

            return "Done."

    def print_unallocated(self, filename):
        """This method prints a list of unallocated people onto the screen.
            Can also print them to a txt file if an optional -o option is specified.
        """

        if filename:
            file = open("models/" + filename + ".txt", "w")
            file.write("UNALLOCATED LIVING SPACES\n")
            file.write(", ".join(self.unallocated_living_spaces))
            file.write("\n")
            file.write("-" * 20)
            file.write("\n\nUNALLOCATED OFFICES\n")
            file.write(", ".join(self.unallocated_offices))
            return "Done."

        else:
            cprint("-" * 20, "blue")
            cprint("UNALLOCATED LIVING SPACES\n", "blue")
            cprint("-" * 20, "blue")
            cprint(", ".join(self.unallocated_living_spaces), "green")
            cprint("-" * 20, "blue")
            cprint("UNALLOCATED OFFICES\n", "blue")
            cprint("-" * 20, "blue")
            cprint(", ".join(self.unallocated_offices), "green")
            return "Done."

    def print_specific_room_allocations(self, room_name):
        """This method prints the names of all the people in room_name on the screen."""

        room_name = room_name.upper()
        all_allocations = dict(self.living_space_allocations)
        all_allocations.update(self.office_allocations)

        if room_name.isalpha() is False:
            return "Invalid input. Try again."

        for room in all_allocations:
            if room_name in room:
                cprint("\n{}\n" .format(room_name), "blue")
                cprint("-" * 20, "blue")
                print("\n")
                cprint(", ".join(all_allocations[room_name]), "green")
        return "Done."

    def print_rooms(self):
        """This method prints all the existing rooms on the screen."""

        cprint("ALL ROOMS:", "blue")
        cprint("-" * 20, "blue")
        cprint(self.all_rooms, "green")
        print("\n")
        cprint("LIVING SPACES:", "blue")
        cprint("-" * 20, "blue")
        cprint(self.living_spaces, "green")
        print("\n")
        cprint("OFFICES:", "blue")
        cprint("-" * 20, "blue")
        cprint(self.offices, "green")
        return "Done."

    def print_fellows(self):
        """This method prints all the existing fellows on the screen."""

        cprint("ALL FELLOWS:", "blue")
        cprint("-" * 20, "blue")
        cprint(self.fellows, "green")
        return "Done."

    def print_staff(self):
        """This method prints all the existing staff on the screen."""

        cprint("ALL STAFF:", "blue")
        cprint("-" * 20, "blue")
        cprint(self.staff, "green")
        return "Done."

    def print_all_people(self):
        """This method prints all the existing people on the screen."""

        cprint("ALL PEOPLE:", "blue")
        cprint("-" * 20, "blue")

        for person in self.fellows + self.staff:
            if person not in self.all_people:
                self.all_people.append(person)

        self.all_people.sort()

        cprint(self.all_people, "green")

        return "Done."

    def load_rooms_file(self, filename):
        """This method creates rooms from a txt file."""

        if filename:

            rooms_file = open("models/" + filename + ".txt")
            rooms = rooms_file.readlines()
            rooms = (content.strip() for content in rooms)

            for room in rooms:
                rooms_data = room.split()

                if len(rooms_data) > 2:
                    return "Invalid input. Try again."

                rooms_name = rooms_data[0]
                rooms_type = rooms_data[1]
                self.create_room(rooms_name, rooms_type)

            return "Rooms successfully loaded from file."

        else:

            return "Filename must be provided. Try again."

    def print_people_identifiers(self):
        """This method prints all the people with their identifiers (IDs) on the screen."""

        for people_id, data in self.person_data.items():
            cprint(str(people_id) + " : " + str(data), "green")

        return "Done."
