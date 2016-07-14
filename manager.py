from jsonhandler import *
from event import *
import uuid

class Manager(object):

    def __init__(self):
        self.j = JsonHandler()

    def add_event(self,event_instance):
        self.j.dump_file({str(uuid.uuid4()): event_instance.__dict__})

    def read_event_by_id(self, event_id):
        storage = self.j.load_file()
        e = Event()
        e.set_name(storage[event_id]['name'])
        print "Name : ",  e.get_name()
        e.set_date(storage[event_id]['date'])
        print "Date : ", e.get_date()
        e.set_city(storage[event_id]['city'])
        print "City :", e.get_city()
        e.set_info(storage[event_id]['info'])
        print "Info : ", e.get_info()

    def update_event_by_id(self, event_id, key, change):
        self.j.update_event_in_file(event_id, key, change)

    def delete_event_by_id(self, event_id):
        self.j.delete_event_in_file(event_id)

    def events_in_date_range(self, date1, date2):
        storage = self.j.load_file()
        for event_id in storage:
            if storage[event_id]['date'] > date1 and  storage[event_id]['date'] < date2 :
                self.read_event_by_id(event_id)
                print "********************"
