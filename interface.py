"""
Usage:
    interface.py save_state [--o=db_name]
    interface.py create_room <room_name> <room_type>
    interface.py add_person <person_name> <job_type> <want_accomodation>
    interface.py allocate_living_space <person_name>
    interface.py allocate_office <person_name>
    interface.py reallocate_person <person_id> <room_name>
    interface.py print_allocations [--o=flename]
    interface.py print_unallocated [--o=filename]
    interface.py load_people [--o=filename]
    interface.py print_specific_room_allocations <room_name>
    interface.py load_state <db_name>
    interface.py print_rooms
    interface.py print_fellows
    interface.py print_staff
    interface.py print_all_people
    interface.py load_rooms_file <filename>
    interface.py print_identifiers

Arguments:
    <db_name> Name of the database
    <room_name> The name of the room
    <room_type> The type of room it can either be an office|living_space
    <person_name> The name of the employee
    <person_id> The ID of the person
    <job_type> The employee's job type it can either be fellow|staff
    <want_accomodation> can either be yes|no
    <database_name> The name of the database
    [--o=filename] The name of the text file to write to or read from

Options:
    -h , --help , Show this screen and exit
"""

import cmd
import os

from docopt import docopt, DocoptExit
from pyfiglet import Figlet
from termcolor import colored, cprint

from database_models import create_db
from models import amity
from sessions import DatabaseSessions


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            cprint('Invalid Command!', 'yellow')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def definition():
    cprint("#" * 100, 'blue')
    font_property = Figlet(font='slant')
    cprint(font_property.renderText('AMITY ALLOCATION'), 'blue')
    cprint("#" * 100, 'blue')
    cprint("This program is supposed to help in the management of the amity facility their events",\
             "blue")
    cprint(__doc__, 'cyan')


#Commands to tun the app
class Amity(cmd.Cmd):
    prompt = '<amity>'

    amity_object = amity.Amity()


    @docopt_cmd
    def do_create_room(self, arg):
        """ Usage: create_room <room_name> <room_type> """
        new_room_name = arg['<room_name>']
        new_room_type = arg['<room_type>']

        cprint(Amity.amity_object.create_room(new_room_name, new_room_type), 'green')


    @docopt_cmd
    def do_add_person(self, arg):
        """ Usage: add_person <person_name> <job_type> <want_accomodation> """
        new_person_name = arg['<person_name>']
        job_type = arg['<job_type>']
        want_accomodation = arg['<want_accomodation>']

        cprint(Amity.amity_object.add_person(new_person_name, job_type.upper(),\
                 want_accomodation.upper()), 'green')


    @docopt_cmd
    def do_allocate_living_space(self, arg):
        """ Usage: allocate_living_space <person_name> """
        person_name = arg['<person_name>']

        cprint(Amity.amity_object.allocate_living_space(person_name.upper()), 'green')


    @docopt_cmd
    def do_allocate_office(self, arg):
        """ Usage: allocate_office <person_name> """
        person_name = arg['<person_name>']

        cprint(Amity.amity_object.allocate_office(person_name.upper()), 'green')


    @docopt_cmd
    def do_reallocate_person(self, arg):
        """ Usage: reallocate_person <person_id> <room_name> """
        person_id = arg['<person_id>']
        room_name = arg['<room_name>']

        cprint(Amity.amity_object.reallocate_person(person_id, room_name.upper()), 'green')


    @docopt_cmd
    def do_print_allocations(self, arg):
        """ Usage: print_allocations [--o=filename] """
        filename = arg['--o']

        cprint(Amity.amity_object.print_allocations(filename), 'green')


    @docopt_cmd
    def do_print_unallocated(self, arg):
        """ Usage: print_unallocated [--o=filename] """
        filename = arg['--o']

        cprint(Amity.amity_object.print_unallocated(filename), 'green')


    @docopt_cmd
    def do_load_people(self, arg):
        """ Usage: load_people [--o=filename] """
        filename = arg['--o']

        cprint(Amity.amity_object.load_people(filename), 'green')


    @docopt_cmd
    def do_print_specific_room_allocations(self, arg):
        """ Usage: print_specific_room_allocations <room_name> """
        room_name = arg['<room_name>']

        cprint(Amity.amity_object.print_specific_room_allocations(room_name), 'green')


    @docopt_cmd
    def do_save_state(self, arg):
        """ Usage: save_state <db_name> """
        database_name = arg['<db_name>']

        create_db(database_name)
        database_object = DatabaseSessions(database_name)
        database_object.add_room()
        database_object.add_office()
        database_object.add_living_space()
        database_object.add_office_allocation()
        database_object.add_living_space_allocation()
        database_object.add_people_unallocated_living_space()
        database_object.add_people_unallocated_office()
        database_object.add_fellow()
        database_object.add_staff()
        database_object.add_person_data()
        database_object.add_room_data()


    @docopt_cmd
    def do_load_state(self, arg):
        """ Usage: load_state <db_name> """
        database_name = arg['<db_name>']

        if os.path.exists("./databases/" + database_name + ".db"):
            database_object = DatabaseSessions(database_name)
            database_object.load_rooms()
            database_object.load_people()
            database_object.load_office_allocations()
            database_object.load_living_space_allocations()
            database_object.load_unallocated_living_space()
            database_object.load_unallocated_office()
            database_object.load_person_data()
            database_object.load_room_data()
        else:
            cprint("Database does not exist. Try again.", 'red')


    @docopt_cmd
    def do_print_rooms(self, arg):
        """ Usage: print_rooms """

        cprint(Amity.amity_object.print_rooms(), 'green')


    @docopt_cmd
    def do_print_fellows(self, arg):
        """ Usage: print_fellows """

        cprint(Amity.amity_object.print_fellows(), 'green')


    @docopt_cmd
    def do_print_staff(self, arg):
        """ Usage: print_staff """

        cprint(Amity.amity_object.print_staff(), 'green')


    @docopt_cmd
    def do_print_all_people(self, arg):
        """ Usage: print_staff """

        cprint(Amity.amity_object.print_all_people(), 'green')


    @docopt_cmd
    def do_load_rooms_file(self, arg):
        """ Usage: load_rooms_file <filename> """

        filename = arg['<filename>']

        cprint(Amity.amity_object.load_rooms_file(filename), 'green')


    @docopt_cmd
    def do_print_identifiers(self, arg):
        """ Usage: print_identifiers """

        cprint(Amity.amity_object.print_people_identifiers(), 'green')


    @docopt_cmd
    def do_quit(self, arg):
        """ Usage: quit """
        exit()



if __name__ == "__main__":
    definition()
    Amity().cmdloop()
