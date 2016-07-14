"""Manager class to handle all the inputs given by user in Main class"""
import uuid
import events
from json_manipulatons import *
from datetime import date


class Manager:
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
        k = uuid.uuid4()
        self.json_instance.write_to_json({str(k): event_instance.__dict__})
        print("Remember this event id:{} for future purposes".format(k))

    def remove_event_by_id(self, event_id):
        self.json_instance.del_from_json(event_id)
        print("Event with id {} deleted".format(event_id))

    def update_event_by_id(self, event_id, field_name, field_value):
        self.json_instance.update_in_json(event_id, field_name, field_value)

    def search_event_by_id(self, event_id):
        data = self.json_instance.read_from_json()
        e = events.Event()
        e.set_name((data[event_id]['a_name']))
        e.set_city((data[event_id]['d_city']))
        e.set_date((data[event_id]['c_date']))
        e.set_info((data[event_id]['b_info']))
        e.set_country(data[event_id]['e_country'])
        for field in e.__dict__:
            print("Event {}:{}".format(field, e.__dict__[field]))

    def today_upcoming_and_completed_events(self):
        temp_data = self.json_instance.read_from_json()
        today_list = []
        upcoming_list = []
        past_list = []
        for key, value in temp_data.items():
            if value['c_date'] == str(date.today()):
                today_list.append(key)
            elif value['c_date'] > str(date.today()):
                upcoming_list.append(key)
            else:
                past_list.append(key)
        print("Today's Event(s):")
        print("-" * 16)
        for k in today_list:
            print('')
            self.search_event_by_id(k)
        print("\nUpcoming Event(s):")
        print("-" * 17)
        for j in upcoming_list:
            print('')
            self.search_event_by_id(j)
        print("\nPast Event(s):")
        print("-" * 13)
        for j in past_list:
            print('')
            self.search_event_by_id(j)

    def list_events_by_date_and_city(self):
        pass

    def list_events_in_date_range(self):
        pass
