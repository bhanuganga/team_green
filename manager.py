import uuid
import json


class Manager:
    def __init__(self):
        self.j = JsonHandler()

    def add_event(self, event_instance):
        k = uuid.uuid4()
        self.j.write_to_json({str(k): event_instance.__dict__})
        print("Remember this event id:{} for future purposes".format(k))

    def remove_event_by_id(self, event_id):
        d = self.j.read_from_json()
        if event_id in d:
            del d[str(event_id)]
            print d
            self.j.write_to_json(d)


class JsonHandler:
    def __init__(self):
        self.file = "abc.json"

    def write_to_json(self, x):
        storage = self.read_from_json()
        with open(self.file, "w+") as f:
            if storage is None:
                json.dump(x, f)
            else:
                storage.update(x)
                json.dump(storage, f, indent=2)

    def read_from_json(self):
        with open(self.file, "r+") as f:
            if f.read() == '':
                return
            else:
                f.seek(0)
                return json.load(f)
