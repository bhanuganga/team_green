from manager import *
import json

class JsonHandler(object):

    def __init__(self):
        self.file_name = "abc.txt"

    def dump_file(self, event_instance):
        storage = self.load_file()
        with open(self.file_name, "w+") as f:
            if storage is None:
                json.dump(event_instance, f)
            else:
                storage.update(event_instance)
                json.dump(storage, f, indent=2)

    def load_file(self):
        with open(self.file_name, "r+") as f:
            if f.read() == '':
                return
            else:
                f.seek(0)
                return json.load(f)

    def update_event_in_file(self,event_id, key, change):
        storage = self.load_file()
        with open(self.file_name, "w+") as f:
            if event_id in storage:
                storage[event_id][key] = change
                json.dump(storage, f, indent=2)
            else:
                print "{} event id does not exist".format(event_id)

    def delete_event_in_file(self, event_id):
        storage = self.load_file()
        with open(self.file_name, "w+") as f:
            if event_id in storage:
                del storage[event_id]
                json.dump(storage, f, indent=2)
            else:
                print "{} event id does not exist".format(event_id)
