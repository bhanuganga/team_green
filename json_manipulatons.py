"""Handles all the json dumps and loads"""
import json


class JsonHandler:
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
        self.file = "data.json"

    def write_to_json(self, x):
        storage = self.read_from_json()
        with open(self.file, "w+") as f:
            if storage is None:
                json.dump(x, f, indent=2)
            else:
                storage.update(x)
                json.dump(storage, f, indent=2, sort_keys=True)

    def read_from_json(self):
        with open(self.file, "r+") as f:
            if f.read() == '':
                return
            else:
                f.seek(0)
                return json.load(f)

    def del_from_json(self, event_id):
        storage = self.read_from_json()
        if storage[event_id]:
            with open(self.file, 'w+') as f:
                del storage[event_id]
                json.dump(storage, f, indent=2)
        else:
            print("No Such Event")

    def update_in_json(self, event_id, field_name, field_value):
        storage = self.read_from_json()
        storage[event_id][field_name] = field_value
        self.write_to_json(storage)
