from manager import *
import datetime
class main(object):
    m=Manager()
    e=Event()
    while True:
        print '1.add_event\n' \
              '2.delete_event_by_id\n' \
              '3.update_event_by_id\n' \
              '4.read_event_by_id\n' \
              '5.upcoming_and_completed_events\n' \
              '6.list_event_by_date_or_by_city\n' \
              '7.list_events_by_date_range\n' \
              '8.exit'
        choice = int(raw_input('enter your choice : '))

        if choice == 1:
            e.set_name(raw_input('enter the event name : '))
            e.set_date(str(datetime.datetime.strptime(raw_input('enter the event date in yyyymmdd : '), '%Y%m%d').date()))
            e.set_city(raw_input('enter the event city : '))
            e.set_info(raw_input('enter the event info : '))
            m.add_event(e)
        elif choice == 2:
            id=raw_input('enter the event id :')
            m.delete_event_by_id(id)

        elif choice == 3:
            id = raw_input("enter the event id number : ")
            field= raw_input('enter the field to change (name or city or info or date) : ')
            if field=='date':
                field_value=str(datetime.datetime.strptime(raw_input('enter the event date in yyyymmdd : '), '%Y%m%d').date())
            else:
                field_value = raw_input('enter the {} : '.format(field))
            m.update_event_by_id(id, field,field_value)

        elif choice == 4:
            id=raw_input('enter the id:')
            m.read_event_by_id(id)

        elif choice == 5:
            pass
        elif choice == 6:
            while True:
                print'1.list_by_date\n' \
                     '2.dist by city\n' \
                     '3.list by date and city\n' \
                     '4.go to previous menu'
                choose =int(raw_input('enter the choice'))
                if choose == 1:
                    date = str(
                        datetime.datetime.strptime(raw_input('enter the event date in yyyymmdd'), '%Y%m%d').date())
                    m.list_event_by_date(date)
                elif choose == 2:
                    city = raw_input('enter the city')
                    m.list_event_by_city(city)
                elif choose == 3:
                    date = str(
                        datetime.datetime.strptime(raw_input('enter the event date in yyyymmdd'), '%Y%m%d').date())
                    city = raw_input('enter the city')
                    m.list_event_by_date_and_city(date, city)
                elif choose == 4:
                    break
                else:
                    print 'invalid choice'
                    print ''

        elif choice == 7:
           pass

        elif choice == 8:
            break

        else:
            print 'invalid choice'
            print ''
