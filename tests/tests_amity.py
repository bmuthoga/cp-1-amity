# coding: utf-8

import os
import unittest

from models.amity import Amity

class Amity_Test(unittest.TestCase):

    def setUp(self):
        self.Amity = Amity()

    def test_create_room(self):
        """Testing if a room is successfully crea†ed."""

        current_count_all_rooms = len(Amity.all_rooms)
        self.Amity.create_room("Narnia", "livingspace")
        new_count_all_rooms = len(Amity.all_rooms)
        self.assertEqual(new_count_all_rooms, current_count_all_rooms+1)

    def test_create_room_living_space(self):
        """Testing if a living space is successfully created."""

        current_count_living_spaces = len(Amity.living_spaces)
        self.Amity.create_room("Mordor", "livingspace")
        new_count_living_spaces = len(Amity.living_spaces)
        self.assertEqual(new_count_living_spaces, current_count_living_spaces+1)

    def test_create_room_office(self):
        """Testing if an office is successfully created."""

        current_count_offices = len(Amity.offices)
        self.Amity.create_room("Oculus", "office")
        new_count_offices = len(Amity.offices)
        self.assertEqual(new_count_offices, current_count_offices+1)

    def test_create_room_invalid_room_type(self):
        """Testing if invalid room type is handled."""

        result = self.Amity.create_room("Mordor", "Offffice")
        self.assertEqual(result, "Invalid room type. Try again.")

    def test_create_room_already_exists(self):
        """Testing if a room already exists."""

        self. Amity.create_room("Hogwarts", "Office")
        result = self.Amity.create_room("Hogwarts", "Office")
        self.assertEqual(result, "HOGWARTS already exists.")

    def test_add_person(self):
        """Testing if a person is successfully created."""

        current_count_all_people = len(Amity.all_people)
        self.Amity.add_person('Batian', 'fellow', 'no')
        new_count_all_people = len(Amity.all_people)
        self.assertEqual(new_count_all_people, current_count_all_people+1)

    def test_add_person_staff(self):
        """Testing if a staff is successfully created."""

        current_count_staff = len(Amity.staff)
        self.Amity.add_person('Batian', 'staff', 'no')
        new_count_staff = len(Amity.staff)
        self.assertEqual(new_count_staff, current_count_staff+1)

    def test_add_person_fellow(self):
        """Testing if a fellow is successfully created."""

        current_count_fellows = len(Amity.fellows)
        self.Amity.add_person('Batian', 'fellow', 'no')
        new_count_fellows = len(Amity.fellows)
        self.assertEqual(new_count_fellows, current_count_fellows+1)

    def test_add_person_invalid_name(self):
        """Testing if invalid person name is handled."""

        result = self.Amity.add_person('Ba23tian', 'fellow', 'no')
        self.assertEqual(result, 'Invalid person name. Try again.')

    def test_add_person_invalid_job_type(self):
        """Testing if invalid job type is handled."""

        result = self.Amity.add_person('Batian', 'fefdgfllow', 'no')
        self.assertEqual(result, 'Invalid job type. Try again.')

    def test_add_person_staff_requests_accomodation(self):
        """Testing if staff requesting accomodation is handled."""

        result = self.Amity.add_person('Batian', 'staff', 'yes')
        self.assertEqual(result, 'No accomodation provided for Staff. Try again.')

    def test_allocate_living_space(self):
        """Testing if fellows are allocated living spaces."""

        self.Amity.create_room("php", "livingspace")
        self.Amity.add_person("Batian", "fellow", "yes")
        self.assertIn("BATIAN", self.Amity.living_space_allocations["PHP"])

    def test_already_allocated_living_space(self):
        """Testing if allocating already allocated living space is handled."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.create_room("php", "livingspace")
        self.Amity.add_person("Batian", "fellow", "yes")
        result = self.Amity.allocate_living_space("BATIAN")
        self.assertEqual(result, "BATIAN already allocated to a living space.")

    def test_no_vacant_living_spaces(self):
        """Testing if no vacant living spaces is handled."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.add_person("Batian", "fellow", "yes")
        self.Amity.add_person("Sharon", "fellow", "yes")
        self.Amity.add_person("Charles", "fellow", "yes")
        self.Amity.add_person("Allan", "fellow", "yes")
        self.Amity.add_person("Kitavi", "fellow", "yes")
        self.Amity.create_room("php", "livingspace")
        self.Amity.allocate_living_space("BATIAN")
        self.Amity.allocate_living_space("SHARON")
        self.Amity.allocate_living_space("CHARLES")
        self.Amity.allocate_living_space("ALLAN")
        result = self.Amity.allocate_living_space("KITAVI")
        self.assertEqual(result, "No vacant living spaces at the moment.")

    def test_allocate_office(self):
        """Testing if people are allocated offices."""

        self.Amity.create_room("java", "office")
        self.Amity.add_person("Batian", "fellow", "no")
        self.assertIn("BATIAN", self.Amity.office_allocations["JAVA"])

    def test_already_allocated_office(self):
        """Testing if allocating already allocated office is handled."""

        result = self.Amity.allocate_office("BATIAN")
        self.assertEqual(result, "BATIAN already allocated to an office.")

    def test_no_vacant_offices(self):
        """Testing if no vacant offices is handled."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.add_person("judy", "fellow", "yes")
        self.Amity.add_person("oliver", "fellow", "yes")
        self.Amity.add_person("sam", "fellow", "yes")
        self.Amity.add_person("ian", "staff", "no")
        self.Amity.add_person("ivan", "fellow", "yes")
        self.Amity.add_person("ken", "staff", "no")
        self.Amity.add_person("alex", "fellow", "yes")
        self.Amity.create_room("php", "office")
        self.Amity.allocate_office("JUDY")
        self.Amity.allocate_office("OLIVER")
        self.Amity.allocate_office("SAM")
        self.Amity.allocate_office("IAN")
        self.Amity.allocate_office("IVAN")
        self.Amity.allocate_office("KEN")
        result = self.Amity.allocate_office("ALEX")
        self.assertEqual(result, "No vacant offices at the moment.")

    def test_reallocate_person(self):
        """Testing if people are reallocated."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.create_room("php", "office")
        self.Amity.add_person("judy", "fellow", "yes")
        self.Amity.create_room("hogwarts", "office")
        result = self.Amity.reallocate_person("F1", "hogwarts")
        self.assertEqual(result, "JUDY has been successfully reallocated to HOGWARTS.")

    def test_reallocate_person_id_does_not_exist(self):
        """Testing if person_id doesn't exist is handled."""

        result = self.Amity.reallocate_person("f25", "hogwarts")
        self.assertEqual(result, "f25 does not exist. Try again.")

    def test_reallocate_room_name_does_not_exist(self):
        """Testing if room_name doesn't exist is handled."""

        result = self.Amity.reallocate_person("F1", "tent")
        self.assertEqual(result, "tent does not exist. Try again.")

    def test_reallocate_staff_to_living_space(self):
        """Testing if staff being reallocated to living space is handled."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.create_room("mordor", "livingspace")
        self.Amity.create_room("php", "office")
        self.Amity.add_person("batianmuthoga", "staff", "n")
        result = self.Amity.reallocate_person("S1", "MORDOR")
        self.assertEqual(result, "Cannot allocate a member of Staff to a living space.")

    def test_reallocate_room_full(self):
        """Testing if reallocating to a full room is handled."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.create_room('oculus', 'livingspace')
        self.Amity.add_person('batian', 'fellow', 'yes')
        self.Amity.add_person('ian', 'fellow', 'yes')
        self.Amity.add_person('sharon', 'fellow', 'yes')
        self.Amity.add_person('judy', 'fellow', 'yes')
        self.Amity.create_room('hogwarts', 'livingspace')
        self.Amity.add_person('ken', 'fellow', 'yes')

        result = self.Amity.reallocate_person('F5', 'OCULUS')
        self.assertEqual(result, "OCULUS already full.")

    def test_reallocate_already_allocated(self):
        """Testing if reallocating a person to a room they're already in is handled."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.create_room('oculus', 'livingspace')
        self.Amity.add_person('batian', 'fellow', 'yes')
        self.Amity.add_person('ian', 'fellow', 'yes')
        self.Amity.add_person('sharon', 'fellow', 'yes')
        self.Amity.add_person('judy', 'fellow', 'yes')

        result = self.Amity.reallocate_person('F4', 'OCULUS')
        self.assertEqual(result, "JUDY already allocated to OCULUS.")

    def test_reallocate_not_yet_allocated(self):
        """Testing if reallocating someone who's not yet allocated is handled."""

        self.Amity.staff = []
        self.Amity.fellows = []
        self.Amity.all_people = []
        self.Amity.all_rooms = []
        self.Amity.offices = []
        self.Amity.living_spaces = []
        self.Amity.office_allocations = {}
        self.Amity.living_space_allocations = {}
        self.Amity.unallocated_living_spaces = []
        self.Amity.unallocated_offices = []
        self.Amity.person_data = {}
        self.Amity.room_data = {}

        self.Amity.add_person('humphrey', 'fellow', 'yes')
        self.Amity.create_room('oculus', 'livingspace')
        self.Amity.add_person('batian', 'fellow', 'yes')
        self.Amity.add_person('ian', 'fellow', 'yes')
        self.Amity.add_person('sharon', 'fellow', 'yes')

        result = self.Amity.reallocate_person('F1', 'OCULUS')
        self.assertEqual(result, "HUMPHREY not yet allocated to any living space.")

    def test_load_people(self):
        """Testing if people successfully added from a file."""

        filename = "load"
        result = self.Amity.load_people(filename)
        self.assertEqual(result, "People successfully loaded.")

    def test_load_people_no_filename(self):
        """Testing if no filename provided is handled."""

        result = self.Amity.load_people("")
        self.assertEqual(result, "Filename must be provided. Try again.")

    def test_load_people_invalid_accomodation(self):
        """Testing if invalid accomodation input is handled."""

        filename = "load_invalid_accomodation"
        result = self.Amity.load_people(filename)
        self.assertEqual(result, "Invalid accomodaton input. Try again.")

    def test_load_people_invalid_number_of_arguments(self):
        """Testing if invalid number of arguments is handled."""

        filename = "load_invalid_num_arguments"
        result = self.Amity.load_people(filename)
        self.assertEqual(result, "Invalid number of arguments input. Try again.")

    def  test_load_people_invalid_job_type(self):
        """Testing if invalid job type is handled."""

        filename = "load_invalid_job_type"
        result = self.Amity.load_people(filename)
        self.assertEqual(result, "Invalid job type. Try again.")

    def test_print_allocations_to_screen(self):
        """Testing if allocations are successfully printed on the screen."""

        filename = ""
        result = self.Amity.print_allocations(filename)
        self.assertEqual(result, "Done.")

    def test_print_allocations_to_file(self):
        """Testing if allocations are successfully printed into a file."""

        filename = "printed_allocations"
        result = self.Amity.print_allocations(filename)
        self.assertTrue(os.path.isfile("models/printed_allocations.txt"))

    def test_print_unallocated_to_screen(self):
        """Testing if unallocations are printed on the screen."""

        filename = ""
        result = self.Amity.print_unallocated(filename)
        self.assertEqual(result, "Done.")

    def test_print_unallocated_to_file(self):
        """Testing if unallocations are printed into a file."""

        filename = "print_unallocated"
        result = self.Amity.print_unallocated(filename)
        self.assertTrue(os.path.isfile("models/print_unallocated.txt"))

    def test_print_specific_room_allocations(self):
        """Testing if specific room allocations are printed on the screen."""

        result = self.Amity.print_specific_room_allocations("oculus")
        self.assertEqual(result, "Done.")

    def test_print_specific_room_allocations_invalid_input(self):
        """Testing if invalid input is handled."""

        result = self.Amity.print_specific_room_allocations("ocu12lus")
        self.assertEqual(result, "Invalid input. Try again.")

    def test_print_rooms(self):
        """Testing if existing rooms are printed on the screen."""

        result = self.Amity.print_rooms()
        self.assertEqual(result, "Done.")

    def test_print_fellows(self):
        """Testing if existing fellows are successfully printed on the screen."""

        result = self.Amity.print_fellows()
        self.assertEqual(result, "Done.")

    def test_print_staff(self):
        """Testing if existing staff are successfully printed on the screen."""

        result = self.Amity.print_staff()
        self.assertEqual(result, "Done.")

    def test_print_all_people(self):
        """Testing if all existing people are successfully printed on the screen."""

        result = self.Amity.print_all_people()
        self.assertEqual(result, "Done.")

    def test_load_rooms_from_file(self):
        """Testing if rooms are successfully created from a file."""

        filename = "rooms"
        result = self.Amity.load_rooms_file(filename)
        self.assertEqual(result, "Rooms successfully loaded from file.")

    def test_load_rooms_from_file_no_filename(self):
        """Testing if no filename provided is handled."""

        filename = ""
        result = self.Amity.load_rooms_file(filename)
        self.assertEqual(result, "Filename must be provided. Try again.")

    def test_load_rooms_from_file_invalid_input(self):
        """Testing if invalid input in file is handled."""

        filename = "rooms_invalid_input"
        result = self.Amity.load_rooms_file(filename)
        self.assertEqual(result, "Invalid input. Try again.")

    def test_print_people_identifiers(self):
        """Testing if all people and their IDs are successfully printed on the screen."""

        result = self.Amity.print_people_identifiers()
        self.assertEqual(result, "Done.")
"""
if __name__ == '__main__':
    unittest.main()
"""