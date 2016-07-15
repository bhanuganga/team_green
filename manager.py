"""Manager class to handle all the inputs given by user in Main class"""
from jsonhandler import *
from event import *
from datetime import *
import uuid


class Manager(object):
    """
        Attribute:
            json_instance: Instance of JsonHandler class
        Methods:
            add_event(),
            remove_event_by_id(id),
            update_event_by_id(event_id, field_name, field_value),
            search_event_by_id(event_id),
            today_upcoming_and_completed_events(),
            list_events_by_date_and_city(),
            list_events_in_date_range().
    """

    def __init__(self):
        self.json_instance = JsonHandler()

    def add_event(self, event_instance):
        id = uuid.uuid4()
        self.json_instance.dump_file({str(id): event_instance.__dict__})
        print "Use this id: {} for future purpose!".format(id)

    def read_event_by_id(self, event_id):
        storage = self.json_instance.load_file()
        if event_id in storage:
            event_instance = Event()
            event_instance.set_name(storage[event_id]['name'])
            print "Name : ",  event_instance.get_name()
            event_instance.set_date(storage[event_id]['date'])
            print "Date : ", event_instance.get_date()
            event_instance.set_city(storage[event_id]['city'])
            print "City : ", event_instance.get_city()
            event_instance.set_info(storage[event_id]['info'])
            print "Info : ", event_instance.get_info()
        else:
            print "{} event id does not exist".format(event_id)

    def update_event_by_id(self, event_id, key, change):
        self.json_instance.update_event_in_file(event_id, key, change)

    def delete_event_by_id(self, event_id):
        self.json_instance.delete_event_in_file(event_id)

    def events_in_date_range(self, date1, date2):
        storage = self.json_instance.load_file()
        print ""
        for event_id in storage:
            if storage[event_id]['date'] > date1 and  storage[event_id]['date'] < date2 :
                self.read_event_by_id(event_id)
                print "********************"

    def list_event_by_date(self,date):
        storage=self.json_instance.load_file()
        count = 1
        for key, value in storage.iteritems():
            if value['date']==date:
                print '{}'.format(count)
                self.read_event_by_id(key)
                count += 1
    def list_event_by_city(self,city):
        storage = self.json_instance.load_file()
        count = 1
        for key, value in storage.iteritems():
            if value['city'] == city:
                print '{}'.format(count)
                self.read_event_by_id(key)
                count += 1

    def list_event_by_date_and_city(self,date,city):
        storage = self.json_instance.load_file()
        count = 1
        for key, value in storage.iteritems():
            if value['date'] == date and value['city']==city:
                print '{}'.format(count)
                self.read_event_by_id(key)
                count += 1

    def today_upcoming_and_completed_events(self):
        temp_data = self.json_instance.load_file()
        today_list = []
        upcoming_list = []
        past_list = []
        for key, value in temp_data.items():
            if value['date'] == str(date.today()):
                today_list.append(key)
            elif value['date'] > str(date.today()):
                upcoming_list.append(key)
            else:
                past_list.append(key)
        print("Today's Event(s):")
        print("-" * 16)
        for k in today_list:
            print('')
            self.read_event_by_id(k)
        print("\nUpcoming Event(s):")
        print("-" * 17)
        for j in upcoming_list:
            print('')
            self.read_event_by_id(j)
        print("\nPast Event(s):")
        print("-" * 13)
        for j in past_list:
            print('')
            self.read_event_by_id(j)