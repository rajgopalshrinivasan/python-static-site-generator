import re 
from yaml import load, FullLoader 
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = r"^(?:-|+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod 
    def load(cls ,string):
        _, fm, content = cls.__regex.split(string,2)
        metadata = load(fm,Loader=FullLoader)
        return cls(metadata,content)

    def __init__(self,metadata ,content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"]
    
    @type.setter
    def x(self, value):
        self.data["type"] = value

    def __getitem__(self,key):
        return self.data[key]

    def __iter__(self):
        return self.data.items()

    def __len__(self):
        return self.data.len()

    def __repr__(self):
        data = {}
        for (key, value) in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)

