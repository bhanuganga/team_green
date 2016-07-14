import manager
from events import *
import datetime


class Main:
    def main(self):
        manager_instance = manager.Manager()

        while True:
            print("\n1.ADD EVENT 2.DELETE EVENT BY ID 3.UPDATE EVENT BY ID 4.READ EVENT BY ID\n5.UPCOMING AND COMPLETED"
                  " EVENTS 6.LIST EVENTS BY DATE AND CITY 7.LIST EVENTS IN DATE RANGE")
            command = int(raw_input("Enter your command:"))

            if command == 1:
                e = Event()
                e.set_name(str(raw_input("Event Name:")))
                e.set_city(str(raw_input("Venue City:")))
                e.set_info(str(raw_input("Event info")))
                e.set_date(raw_input("Date:"))
                manager_instance.add_event(e)

            elif command == 2:
                event_id = raw_input("Event Id:")
                manager_instance.remove_event_by_id(event_id)

x = Main()
x.main()
