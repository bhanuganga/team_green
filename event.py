class Event(object):

    def __init__(self):
        self.name = ""
        self.date = ""
        self.city = ""
        self.info = ""

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_info(self, info):
        self.info = info

    def get_info(self):
        return self.info

    def to_json(self):
        pass