from event import *
from manager import *
from datetime import date


class Main(object):

    m = Manager()
    e = Event()

    while(1):
        print "1: add_event  2: read_event  3: update_event  4: delete_event  5: list_events_in_date_range "

        choice = int(raw_input("choice"))

        if choice == 1:
            e.set_name(raw_input("enter name :"))
            e.set_city(raw_input("enter city :"))
            e.set_info(raw_input("enter info :"))
            e.set_date(str(date(int(raw_input("enter year(yyyy) :")),
                                int(raw_input("enter month(mm) :")),
                                int(raw_input("enter day(dd) :")))))
            m.add_event(e)

        if choice == 2:
            m.read_event_by_id(raw_input("enter the event id :"))

        if choice == 3:
            m.update_event_by_id(raw_input("enter the event id :"),raw_input("enter the key to be changed :"), raw_input("enter the changes"))

        if choice == 4:
            m.delete_event_by_id(raw_input("enter the event id :"))

        if choice == 5:
            m.events_in_date_range(str(date(int(raw_input("enter year(yyyy) :")),
                                            int(raw_input("enter month(mm) :")),
                                            int(raw_input("enter day(dd) :")))),
                                   str(date(int(raw_input("enter year(yyyy) :")),
                                            int(raw_input("enter month(mm) :")),
                                            int(raw_input("enter day(dd) :")))))

        elif choice == 10:
            break

#######################################

if __name__ == "__main__":
    Main()
