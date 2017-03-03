from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from termcolor import colored, cprint

from models.amity import Amity
from database_models import AmityRooms, AmityOffices, AmityLivingSpaces,\
    AmityOfficeAllocations, AmityLivingSpaceAllocations, AmityUnallocatedLivingSpace,\
    AmityUnallocatedOffice, AmityFellows, AmityStaff, AmityPersonData, AmityRoomData


class DatabaseSessions(object):
    def __init__(self, db_name):
        directory = "databases/"
        engine = create_engine('sqlite:///' + directory + db_name + '.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_room(self):
        """ Adds data to the table AmityRooms with data from Amity.all_rooms[] """

        for room in Amity.all_rooms:
            room_object = self.session.query(AmityRooms).filter_by(room_name=room).first()

            if room_object is None:
                new_room = AmityRooms(room_name=room)
                self.session.add(new_room)
                self.session.commit()

            else:
                self.session.commit()

        cprint("Rooms saved successfully!", 'green')

    def add_office(self):
        """ This method adds an office to the table AmityOffices with data from Amity.offices[] """

        for office in Amity.offices:
            office_object = self.session.query(AmityOffices).filter_by(office_name=office).first()

            if office_object is None:
                new_office = AmityOffices(office_name=office)
                self.session.add(new_office)
                self.session.commit()

            else:
                self.session.commit()

        cprint("Offices saved successfully!", 'green')

    def add_living_space(self):
        """ This method adds a living space to the table AmityLivingSpaces with data from
            Amity.living_spaces[] """

        for living_space in Amity.living_spaces:
            living_space_object = self.session.query(AmityLivingSpaces).\
                filter_by(livingspace_name=living_space).first()

            if living_space_object is None:
                new_living_space = AmityLivingSpaces(livingspace_name=living_space)
                self.session.add(new_living_space)
                self.session.commit()

            else:
                self.session.commit()

        cprint("Living spaces saved successfully!", 'green')

    def add_office_allocation(self):
        """ This method adds an office and its allocated members to the table AmityOfficeAllocations
            with data from Amity.office_allocations{} """

        for office_name, allocated_people in Amity.office_allocations.items():
            room_object = self.session.query(AmityOfficeAllocations).\
                filter_by(office_name=office_name).first()

            if room_object is None:
                joint_allocated_people = ",".join(allocated_people)
                new_office = AmityOfficeAllocations(office_name=office_name,\
                    allocated_people=joint_allocated_people)
                self.session.add(new_office)
                self.session.commit()

            else:
                joint_allocated_people = ",".join(allocated_people)
                room_object.office_name = office_name
                room_object.allocated_people = joint_allocated_people
                self.session.commit()

        cprint("Office allocations saved successfully!", 'green')

    def add_living_space_allocation(self):
        """ This method adds a living space and its allocated members to the table
            AmityLivingSpaceAllocations with data from Amity.living_space_allocations{} """

        for livingspace_name, allocated_people in Amity.living_space_allocations.items():
            room_object = self.session.query(AmityLivingSpaceAllocations).\
                            filter_by(livingspace_name=livingspace_name).first()

            if room_object is None:
                joint_allocated_people = ','.join(allocated_people)
                new_living_space = AmityLivingSpaceAllocations(livingspace_name=livingspace_name,\
                                    allocated_people=joint_allocated_people)
                self.session.add(new_living_space)
                self.session.commit()

            else:
                joint_allocated_people = ','.join(allocated_people)
                room_object.livingspace_name = livingspace_name
                room_object.allocated_people = joint_allocated_people
                self.session.commit()

        cprint("Living space allocations saved successfully!", 'green')


    def add_people_unallocated_living_space(self):
        """ This method adds fellows who are not allocated living spaces to the table
            AmityUnallocatedLivingSpace with data from Amity.unallocated_living_spaces[] """

        for person in Amity.unallocated_living_spaces:
            person_object = self.session.query(AmityUnallocatedLivingSpace).\
                                filter_by(unallocated_name=person).first()

            if person_object is None:
                new_person = AmityUnallocatedLivingSpace(unallocated_name=person)
                self.session.add(new_person)
                self.session.commit()

            else:
                self.session.commit()

        cprint("Living space unallocations saved successfully!", 'green')

    def add_people_unallocated_office(self):
        """ This method adds people who are not allocated offices to the table
            AmityUnallocatedOffice with data from unallocated_offices[] """

        for person in Amity.unallocated_offices:
            person_object = self.session.query(AmityUnallocatedOffice).\
                                filter_by(unallocated_name=person).first()

            if person_object is None:
                new_person = AmityUnallocatedOffice(unallocated_name=person)
                self.session.add(new_person)
                self.session.commit()

            else:
                self.session.commit()

        cprint("Office unallocations saved successfully!", 'green')

    def add_fellow(self):
        """ This method adds fellows to the AmityFellows table with data from Amity.fellows[] """

        for fellow in Amity.fellows:
            fellow_object = self.session.query(AmityFellows).filter_by(fellow_name=fellow).first()

            if fellow_object is None:
                new_fellow = AmityFellows(fellow_name=fellow)
                self.session.add(new_fellow)
                self.session.commit()

            else:
                self.session.commit()

        cprint("Fellows saved successfully!", 'green')

    def add_staff(self):
        """ This method adds staff to the AmityStaff table with data from Amity.staff[] """

        for staff in Amity.staff:
            staff_object = self.session.query(AmityStaff).filter_by(staff_name=staff).first()

            if staff_object is None:
                new_staff = AmityStaff(staff_name=staff)
                self.session.add(new_staff)
                self.session.commit()

            else:
                self.session.commit()

        cprint("Staff saved successfully!", 'green')

    def add_person_data(self):
        """ This method adds person data to the AmityPersonData table with data from
            Amity.person_data{} """

        for person_id, person_details in Amity.person_data.items():
            person_id_object = self.session.query(AmityPersonData).\
                                filter_by(person_id=person_id).first()

            if person_id_object is None:
                new_person_data = AmityPersonData(person_id=person_id,\
                                    person_name=Amity.person_data[person_id][0],\
                                    person_job_type=Amity.person_data[person_id][1],\
                                    person_wants_accomodation=Amity.person_data[person_id][2])
                self.session.add(new_person_data)
                self.session.commit()

            else:
                person_id_object.person_id = person_id
                person_id_object.person_details = person_details
                self.session.commit()

        cprint("Person data saved successfully!", 'green')

    def add_room_data(self):
        """ This method adds room data to the AmityRoomData table with data from
            Amity.room_data{} """

        for room_name, room_details in Amity.room_data.items():
            room_name_object = self.session.query(AmityRoomData).\
                                filter_by(room_name=room_name).first()

            if room_name_object is None:
                new_room_data = AmityRoomData(room_name=room_name,\
                                    room_type=Amity.room_data[room_name][0],\
                                    room_capacity=Amity.room_data[room_name][1])
                self.session.add(new_room_data)
                self.session.commit()

            else:
                room_name_object.room_name = room_name
                room_name_object.room_details = room_details
                self.session.commit()

        cprint("Room data saved successfully!", 'green')

    def load_rooms(self):
        """ This method returns rooms stored from the database into the application. """

        rooms = self.session.query(AmityRooms).all()
        living_spaces = self.session.query(AmityLivingSpaces).all()
        offices = self.session.query(AmityOffices).all()

        for room in rooms:
            Amity.all_rooms.append(room.room_name)

        for living_space in living_spaces:
            Amity.living_spaces.append(living_space.livingspace_name)

        for office in offices:
            Amity.offices.append(office.office_name)

        cprint("Rooms loaded successfully!", 'green')

    def load_people(self):
        """ This method returns people stored from the database into the application. """

        fellows = self.session.query(AmityFellows).all()
        staff = self.session.query(AmityStaff).all()

        for fellow in fellows:
            Amity.fellows.append(fellow.fellow_name)

        for single_staff in staff:
            Amity.staff.append(single_staff.staff_name)

        cprint("People loaded successfully!", 'green')

    def load_office_allocations(self):
        """ This method returns office allocations from the database into the application. """

        office_allocations = self.session.query(AmityOfficeAllocations).all()
        empty_people = []

        for office_allocation in office_allocations:
            office_name = office_allocation.office_name
            allocated_people = office_allocation.allocated_people

            if allocated_people is None:
                Amity.office_allocations[office_name] = empty_people

            allocated_people = allocated_people.split(",")
            Amity.office_allocations[office_name] = allocated_people

        cprint("Office allocations loaded successfully!", 'green')

    def load_living_space_allocations(self):
        """ This method returns living space allocations from the database into the application. """

        living_space_allocations = self.session.query(AmityLivingSpaceAllocations).all()
        empty_people = []

        for living_space_allocation in living_space_allocations:
            living_space_name = living_space_allocation.livingspace_name
            allocated_people = living_space_allocation.allocated_people

            if allocated_people is None:
                Amity.living_space_allocations[living_space_name] = empty_people

            allocated_people = allocated_people.split(",")
            Amity.living_space_allocations[living_space_name] = allocated_people

        cprint("Living space allocations loaded successfully!", 'green')

    def load_unallocated_living_space(self):
        """ This method returns fellows not allocated living space from the database into
            the application. """

        living_space_unallocations = self.session.query(AmityUnallocatedLivingSpace).all()

        for living_space_unallocation in living_space_unallocations:
            Amity.unallocated_living_spaces.append(living_space_unallocation.unallocated_name)

        cprint("Living space unallocations loaded successfully!", 'green')

    def load_unallocated_office(self):
        """ This method returns people not allocated office from the database into the
            application. """

        office_unallocations = self.session.query(AmityUnallocatedOffice).all()

        for office_unallocation in office_unallocations:
            Amity.unallocated_offices.append(office_unallocation.unallocated_name)

        cprint("Office unallocations loaded successfully!", 'green')

    def load_person_data(self):
        """ This method returns person data from the database into the application. """

        person_data = self.session.query(AmityPersonData).all()

        for single_person in person_data:
            person_id = single_person.person_id
            person_name = single_person.person_name
            person_job_type = single_person.person_job_type
            person_wants_accomodation = single_person.person_wants_accomodation
            Amity.person_data[person_id] = [person_name, person_job_type, person_wants_accomodation]

        cprint("Person data loaded successfully!", 'green')

    def load_room_data(self):
        """ This method returns room data from the database into the application. """

        room_data = self.session.query(AmityRoomData).all()

        for single_room in room_data:
            room_name = single_room.room_name
            room_type = single_room.room_type
            room_capacity = single_room.room_capacity
            Amity.room_data[room_name] = [room_type, room_capacity]

        cprint("Room data loaded successfully!", 'green')
