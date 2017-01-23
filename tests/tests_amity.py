import unittest
from models.amity import Amity

class Amity_Test(unittest.TestCase):

    def setUp(self):
        self.Amity = Amity()

    def test_create_room(self):
        current_count_rooms = len(Amity.rooms)
        Amity.create_room("Hogwarts", "Living space")
        new_count_rooms = len(Amity.rooms)
        self.assertEqual(new_count_rooms, current_count_rooms+1)

    def test_create_room_living_space(self):
        current_count_living_spaces = len(Amity.living_spaces)
        Amity.create_room("Narnia", "Living space")
        new_count_living_spaces = len(Amity.living_spaces)
        self.assertEqual(new_count_living_spaces, current_count_living_spaces+1)

    def test_create_room_office(self):
        current_count_offices = len(Amity.offices)
        Amity.create_room("Oculus", "Office")
        new_count_offices = len(Amity.offices)
        self.assertEqual(new_count_offices, current_count_offices+1)

    def test_create_room_invalid_room_type(self):
        self.assertRaises(ValueError, Amity.create_room, "Narnia", "Kitchen")

    def test_add_person(self):
        current_count_persons = len(Amity.all_people)
        Amity.add_person("Batian", "Yes", "STAFF")
        new_count_persons = len(Amity.all_people)
        self.assertEqual(new_count_persons, current_count_persons+1)

    def test_add_person_invalid_job_type(self):
        self.assertRaises(ValueError, Amity.add_person, "Muthoga", "No", "STAFFF")

"""
if __name__ == '__main__':
    unittest.main()
"""