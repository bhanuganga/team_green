"""Event class to create a structure"""
class Event(object):
    """Event class
    Attributes:
        name, information, date, city, country
    Methods:
        set_value(input), get_value() are common for all attributes, where value=Attribute.
        """

    def __init__(self):
        self.a_name = None
        self.b_info = None
        self.c_date = None
        self.d_city = None
        self.e_country = None

    def set_name(self, inbound):
        self.a_name = inbound

    def get_name(self):
        return self.a_name

    def set_info(self, inbound):
        self.b_info = inbound

    def get_info(self):
        return self.b_info

    def set_date(self, inbound):
        self.c_date = inbound

    def get_date(self):
        return self.c_date

    def set_city(self, inbound):
        self.d_city = inbound

    def get_city(self):
        return self.d_city

    def set_country(self, inbound):
        self.e_country = inbound

    def get_country(self):
        return self.e_country

#   def to_json(self):
#        return {uuid.uuid4():{'name':self.a_name,'unfo':self.b_info,'c_date':self.c_date,'d_city':self.d_city}}
