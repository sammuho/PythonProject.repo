import json
#with open('person.json','r') as f:
#    person=json.load(f)
#    print(person)
def encode_complex(z):
    if isinstance(z, complex):
        return {z.__class__.__name__: True, "real":z.real, "imag": z.imag}
        #just the key of the class name is important, the value can be arbitrary.
        
    else:
        raise TypeError(f"Object of type '{z.__class__.__name__}' is not JSON serializable")
z = 5 + 9j
zJSON = json.dumps(z, default=encode_complex)
print(zJSON)
