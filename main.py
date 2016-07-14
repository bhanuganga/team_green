"""Only user inputs with predefined list of choices."""
import manager
from events import *
from datetime import date


class Main:
    manager_instance = manager.Manager()

    while True:
        print("\n1.ADD EVENT 2.DELETE EVENT BY ID 3.UPDATE EVENT BY ID 4.READ EVENT BY ID\n5.UPCOMING AND COMPLETED"
              "EVENTS 6.LIST EVENTS BY DATE AND CITY 7.LIST EVENTS IN DATE RANGE 8.EXIT")
        command = int(raw_input("Enter your command:"))

        if command == 8:
            break

        elif command == 1:
            e = Event()
            e.set_name(str(raw_input("Event Name:")))
            e.set_city(str(raw_input("Venue City:")))
            e.set_info(str(raw_input("Event Info:")))
            e.set_date(str(date(int(raw_input("Year(YYYY):")),
                                int(raw_input("Month(MM):")),
                                int(raw_input("Day(DD):")))))
            e.set_country(str(raw_input('Country:')))
            manager_instance.add_event(e)

        elif command == 2:
            event_id = raw_input("Enter event Id:")
            manager_instance.remove_event_by_id(event_id)

        elif command == 3:
            event_id = raw_input("Enter event Id:")
            field_name = raw_input("Enter the field name you'd like to update name | d_city | b_info | c_date:")
            if field_name != date:
                field_value = raw_input("Enter new {}:".format(field_name))
            else:
                field_value = str(date(int(raw_input("Year(YYYY):")),
                                       int(raw_input("Month(MM):")),
                                       int(raw_input("Day(DD):"))))
            manager_instance.update_event_by_id(event_id, field_name, field_value)

        elif command == 4:
            event_id = raw_input("Enter event Id:")
            manager_instance.search_event_by_id(event_id)

        elif command == 5:
            manager_instance.today_upcoming_and_completed_events()

        elif command == 6:
            pass

        elif command == 7:
            pass

        elif command == 8:
            pass

        else:
            pass


if __name__ == "__main__":
    Main()
