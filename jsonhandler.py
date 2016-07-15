"""Handles all the json dumps and loads"""
import json

class JsonHandler(object):
    """
       Attributes:
           file: File name to which json objects are stored
       Methods:
           write_to_json(object),
           read_from_json(): Used by all other methods,
           del_from_json(event_id),
           update_in_json(event_id, field_name, field_value).
       """

    def __init__(self):
        self.file_name = "data.json"

    def dump_file(self, x):
        storage = self.load_file()
        with open(self.file_name, "w+") as f:
            if storage is None:
                json.dump(x, f, indent=2)
            else:
                storage.update(x)
                json.dump(storage, f, indent=2)

    def load_file(self):
        with open(self.file_name, "r+") as f:
            if f.read() == '':
                return
            else:
                f.seek(0)
                return json.load(f)

    def update_event_in_file(self, event_id, key, change):
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
