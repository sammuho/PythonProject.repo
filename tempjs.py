import json
class User:
    # custom Class with all instance variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name=name
        self.age=age 
        self.active=active
        self.balance=balance
        self.friends=friends

class Player:
    #other custom class
    def __init__(self, name, nickname, level):
        self.name=name
        self.nickname=nickname
        self.level=level

def encode_obj(obj):
    """takes in a custom object and returns a dictionary representation of object. This dict representation also includes object's module and names."""
    #populate the dictionary with object meta data
    obj_dict={"__class__": obj.__class__.__name__,"__module__": obj.__module__}
    #populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
    
    return obj_dict

def decode_dct(dct):
    """Takes in a dict and rturns a custom object associated with the dict.it makes use of the module__module__ and __class__ metadata inthe dictinary to know which object tupe to create"""
    if "__class__" in dct:
        #pop ensures we remove metadata from the dct to leave only the instance arguments
        class_name=dct.pop("__class__")
        #module data
        module_name=dct.pop("__module__")
        #we use the built in __import__funct since the module name is not known at run time
        module=__import__(module_name)
        #get class from module 
        class_=getattr(module, class_name)
        #use dictionary unpacking to initialize the object
        # note: this only works if all the init__arguments of class are exact the dict keye
        obj=class_(**dct)
    else:
        obj=dct
    return obj
#User class works with oure encoding and decoding methods
user= User(name= "John", age=28, friends=["Jane","Tom"], balance=20.70, active=True)
userJSON=json.dumps(user, default=encode_obj, indent=4, sort_keys=True)
print(userJSON)
user_decoded=json.loads(userJSON, object_hook=decode_dct)
print(type(user_decoded))
#player calass also works with custom encoding and decoding
player=Player('Max', 'Max1234', 5)
playerJSON=json.dumps(player, default=encode_obj,indent=4, sort_keys=True)
print(playerJSON)
player_decoded=json.loads(playerJSON, object_hook=decode_dct)
print(type(player_decoded))
