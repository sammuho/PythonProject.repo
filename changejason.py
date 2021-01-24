import json

class User:
    def __init__(self,name, age):
        self.name=name
        self.age=age
user=User('Max', 27)

#to encode user first way
def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of Type User is not json serializable')
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

#way 2 to decode
from json import JSONEncoder
class userEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
userJSON = json.dumps(user, cls=userEncoder) 
print(userJSON)
userJSON=userEncoder().encode(user)

#decode back
user=json.loads(userJSON)