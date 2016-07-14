import json
from events import *
class Json_Handling(object):
    e=Event()

    def __init__(self):
        self.file='abc.json'
    def write_file(self, x):
        s=self.read_file()
        with open(self.file,'w+') as f:
            if s is None:
                json.dump(x,f)
            else:
                s.update(x)
                json.dump(s,f,indent=2)
    def read_file(self):
        with open(self.file,'r+') as f:
            if f.read()=='':
                return
            else:
                f.seek(0)
                return json.load(f)

    def update_file(self,id,x,b):
        s = self.read_file()
        with open(self.file, 'w+') as f:
            s[id][x]=b
            json.dump(s, f, indent=2)

    def delete_file(self,id):
        s=self.read_file()
        with open(self.file,'w+') as f:
            if s.has_key(id):
                del s[id]
                json.dump(s,f,indent=2)
