
import uuid
import datetime

class Event(object):
    def __init__(self):
        self.name = None
        self.info = None
        self.date = None
        self.city = None

    def set_name(self, inbound):
        self.name = inbound

    def get_name(self):
        return self.name

    def set_info(self, inbound):
        self.info = inbound

    def get_info(self):
        return self.info

    def set_date(self, inbound):
        self.date = inbound

    def get_date(self):
        return self.date

    def set_city(self, inbound):
        self.city = inbound

    def get_city(self):
        return self.city

#   def to_json(self):
        #return {uuid.uuid4():{'name':self.name,'unfo':self.info,'date':self.date,'city':self.city}}

