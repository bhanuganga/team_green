from event import *
from manager import *
from datetime import date


class Main(object):

    m = Manager()
    e = Event()

    while(1):
        print "1: add_event  2: read_event  3: update_event  4: delete_event  5: upcoming_and_completed events  6: list_event_by_date_or_by_city  7: list_events_in_date_range  8: Exit"

        choice = int(raw_input("choice"))

        if choice == 1:
            e.set_name(raw_input("enter name :"))
            e.set_city(raw_input("enter city :"))
            e.set_info(raw_input("enter info :"))
            e.set_date(str(date(int(raw_input("enter year(yyyy) :")),
                                int(raw_input("enter month(mm) :")),
                                int(raw_input("enter day(dd) :")))))
            m.add_event(e)

        elif choice == 2:
            m.read_event_by_id(raw_input("enter the event id :"))

        elif choice == 3:
            m.update_event_by_id(raw_input("enter the event id :"),raw_input("enter the key to be changed :"), raw_input("enter the changes"))

        elif choice == 4:
            m.delete_event_by_id(raw_input("enter the event id :"))

        elif choice == 5:
            m.events_in_date_range(str(date(int(raw_input("enter year(yyyy) :")),
                                            int(raw_input("enter month(mm) :")),
                                            int(raw_input("enter day(dd) :")))),
                                   str(date(int(raw_input("enter year(yyyy) :")),
                                            int(raw_input("enter month(mm) :")),
                                            int(raw_input("enter day(dd) :")))))

        elif choice == 6:
            pass

        elif choice == 7:
            pass

        elif choice == 8:
            break

        else:
            print "Invalid choice."

#######################################

if __name__ == "__main__":
    Main()
