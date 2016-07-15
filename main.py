"""Only user inputs with predefined list of choices."""

from event import *
from manager import *
from datetime import date


class Main(object):

    manager_instance = Manager()

    while (1):
        print "1: add_event  2: read_event  3: update_event  4: delete_event  5: upcoming_and_completed events  " \
              "6: list_event_by_date_or_by_city  7: list_events_in_date_range  8: Exit"

        choice = int(raw_input("choice:"))

        if choice == 1:
            event_instance = Event()
            event_instance.set_name(raw_input("enter event name :"))
            event_instance.set_city(raw_input("enter city :"))
            event_instance.set_info(raw_input("enter info :"))
            event_instance.set_date(str(date(int(raw_input("enter year(yyyy) :")),
                                             int(raw_input("enter month(mm) :")),
                                             int(raw_input("enter day(dd) :")))))
            manager_instance.add_event(event_instance)

        elif choice == 2:
            manager_instance.read_event_by_id(raw_input("enter the event id :"))

        elif choice == 3:
            manager_instance.update_event_by_id(raw_input("enter the event id :"),
                                                raw_input("enter the key to be changed :"),
                                                raw_input("enter the changes"))

        elif choice == 4:
            manager_instance.delete_event_by_id(raw_input("enter the event id :"))

        elif choice == 5:
            manager_instance.today_upcoming_and_completed_events()

        elif choice == 6:
            while True:
                print'1.list_by_date\n' \
                     '2.dist by city\n' \
                     '3.list by date and city\n' \
                     '4.go to previous menu'
                choose = int(raw_input('enter the choice'))
                if choose == 1:
                    manager_instance.list_event_by_date(str(date(int(raw_input("enter year(yyyy) :")),
                                                                 int(raw_input("enter month(mm) :")),
                                                                 int(raw_input("enter day(dd) :")))))
                elif choose == 2:
                    city = raw_input('enter the city')
                    manager_instance.list_event_by_city(city)
                elif choose == 3:
                    manager_instance.list_event_by_date_and_city(str(date(int(raw_input("enter year(yyyy) :")),
                                                                          int(raw_input("enter month(mm) :")),
                                                                          int(raw_input("enter day(dd) :")))),
                                                                 city=raw_input('enter the city')
                                                                 )
                elif choose == 4:
                    break
                else:
                    print 'invalid choice'
                    print ''


        elif choice == 7:
            manager_instance.events_in_date_range(str(date(int(raw_input("enter year(yyyy) :")),
                                                           int(raw_input("enter month(mm) :")),
                                                           int(raw_input("enter day(dd) :")))),
                                                  str(date(int(raw_input("enter year(yyyy) :")),
                                                           int(raw_input("enter month(mm) :")),
                                                           int(raw_input("enter day(dd) :")))))


        elif choice == 8:
            break

        else:
            print "Invalid choice."


#######################################

if __name__ == "__main__":
    Main()
