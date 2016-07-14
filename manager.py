from jsonhandler import *
import uuid

class Manager(object):

    def __init__(self):
        self.j=Json_Handling

    def add_event(self,event_instance):
        id=uuid.uuid4()
        self.j().write_file({str(id):event_instance.__dict__})
        print 'note this unique id:{} for future use '.format(id)

    def delete_event_by_id(self,id):
        self.j().delete_file(id)
        print 'event with id {} is deleted'.format(id)

    def update_event_by_id(self,id,x,b):
        self.j().update_file(id,x,b)
        print 'event with id {} updated'.format(id)


    def read_event_by_id(self,id):
        s=self.j().read_file()
        e=Event()
        e.set_name(s[id]['name'])
        print 'name : ', e.get_name()
        e.set_date(s[id]['date'])
        print 'date : ',e.get_date()
        e.set_city(s[id]['city'])
        print 'city :',e.get_city()
        e.set_info(s[id]['info'])
        print 'info :',e.get_info()

    def upcoming_and_completed_events(self):
        pass

    def list_event_by_date(self,date):
        s=self.j().read_file()
        c=1
        for a,v in s.iteritems():
            if v['date']==date:
                print '{}'.format(c)
                self.read_event_by_id(a)
                c+=1
    def list_event_by_city(self,city):
        s = self.j().read_file()
        c = 1
        for a, v in s.iteritems():
            if v['city'] == city:
                print '{}'.format(c)
                self.read_event_by_id(a)
                c += 1

    def list_event_by_date_and_city(self,date,city):
        s = self.j().read_file()
        c = 1
        for a, v in s.iteritems():
            if v['date'] == date and v['city']==city:
                print '{}'.format(c)
                self.read_event_by_id(a)
                c += 1

    def list_events_by_date_range(self,from_date,to_date):
        pass
