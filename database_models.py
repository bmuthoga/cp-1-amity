import os

from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class AmityRooms(Base):
    __tablename__ = "AmityRooms"
    room_name = Column(String(25), primary_key=True)

class AmityOffices(Base):
    __tablename__ = "AmityOffices"
    office_name = Column(String(25), primary_key=True)

class AmityLivingSpaces(Base):
    __tablename__ = "AmityLivingSpaces"
    livingspace_name = Column(String(25), primary_key=True)

class AmityOfficeAllocations(Base):
    __tablename__ = "AmityOfficeAllocations"
    office_name = Column(String(25), primary_key=True)
    allocated_people = Column(String(25))

class AmityLivingSpaceAllocations(Base):
    __tablename__ = "AmityLivingSpaceAllocations"
    livingspace_name = Column(String(25), primary_key=True)
    allocated_people = Column(String(250))

class AmityUnallocatedLivingSpace(Base):
    __tablename__ = "AmityUnallocatedLivingSpace"
    unallocated_name = Column(String(25), primary_key=True)

class AmityUnallocatedOffice(Base):
    __tablename__ = "AmityUnallocatedOffice"
    unallocated_name = Column(String(25), primary_key=True)

class AmityFellows(Base):
    __tablename__ = "AmityFellows"
    fellow_name = Column(String(25), primary_key=True)

class AmityStaff(Base):
    __tablename__ = "AmityStaff"
    staff_name = Column(String(25), primary_key=True)

class AmityPersonData(Base):
    __tablename__ = "AmityPersonData"
    person_id = Column(String(25), primary_key=True)
    person_name = Column(String(25))
    person_job_type = Column(String(25))
    person_wants_accomodation = Column(String(25))

class AmityRoomData(Base):
    __tablename__ = "AmityRoomData"
    room_name = Column(String(25), primary_key=True)
    room_type = Column(String(25))
    room_capacity = Column(Integer)

def create_db(dbname):
    database_directory = "databases/"
    engine = create_engine('sqlite:///' + database_directory + dbname + '.db')
    return Base.metadata.create_all(engine)

